#load_data  = load json into the python
#save_data  = save python data into json
#add_mood_entry = add a mood entry into the data
#add_conversation = record user bot conversation
#get_coping_strategies = retrieve a relaxation technique


import json
from datetime import datetime
import uuid
from typing import Optional, List, Dict, Any

def _now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def load_data(file_path: str) -> Dict[str, Any]:
    """
    Load JSON data from file_path. Returns an empty template if file missing or invalid.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Basic template compatible with expected schema
        return {
            "metadata": {},
            "bot": {},
            "users": [],
            "mood_journal": [],
            "conversations": [],
            "coping_strategies": [],
            "resources": {},
            "analytics": {},
            "maintenance": {}
        }

def save_data(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to file_path (pretty-printed).
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def _make_id(prefix: str) -> str:
    return f"{prefix}-{datetime.utcnow().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"

def add_mood_entry(
    data: Dict[str, Any],
    user_id: str,
    mood_score: int,
    mood_label: Optional[str] = None,
    tags: Optional[List[str]] = None,
    note: str = "",
    activities: Optional[List[str]] = None,
    triggers: Optional[List[str]] = None,
    interventions_used: Optional[List[str]] = None,
    timestamp: Optional[str] = None
) -> Dict[str, Any]:
    """
    Add a mood entry to data['mood_journal'] and return the created entry.
    """
    if "mood_journal" not in data:
        data["mood_journal"] = []

    entry = {
        "entry_id": _make_id("mj"),
        "user_id": user_id,
        "timestamp": timestamp or _now_iso(),
        "mood_score": int(mood_score),
        "mood_label": mood_label or "",
        "tags": tags or [],
        "note": note,
        "activities": activities or [],
        "triggers": triggers or [],
        "interventions_used": interventions_used or []
    }

    data["mood_journal"].append(entry)

    # update simple analytics if present
    try:
        analytics = data.setdefault("analytics", {})
        counts = analytics.setdefault("conversation_counts", {})
        # keep total_sessions as-is; update nothing here except last_analyzed_at placeholder
        analytics.setdefault("last_analyzed_at", None)
    except Exception:
        pass

    return entry

def add_conversation(
    data: Dict[str, Any],
    user_id: str,
    messages: List[Dict[str, Any]],
    started_at: Optional[str] = None,
    ended_at: Optional[str] = None,
    session_summary: Optional[str] = None,
    risk_assessment: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Record a conversation session. messages is a list of dicts with (sender, text, optional timestamp, optional intent).
    Each message will receive a msg_id if missing.
    """
    if "conversations" not in data:
        data["conversations"] = []

    session_id = _make_id("sess")
    now = _now_iso()
    started = started_at or (messages[0].get("timestamp") if messages else now) or now
    ended = ended_at or (messages[-1].get("timestamp") if messages else now) or now

    normalized_messages = []
    for i, m in enumerate(messages, start=1):
        msg = {
            "msg_id": m.get("msg_id") or f"m-{i}-{uuid.uuid4().hex[:6]}",
            "sender": m.get("sender", "user"),
            "text": m.get("text", ""),
            "timestamp": m.get("timestamp") or _now_iso(),
            "intent": m.get("intent"),
            "sentiment_score": m.get("sentiment_score"),
            "flagged": bool(m.get("flagged", False))
        }
        normalized_messages.append(msg)

    conversation = {
        "session_id": session_id,
        "user_id": user_id,
        "started_at": started,
        "ended_at": ended,
        "messages": normalized_messages,
        "session_summary": session_summary or "",
        "risk_assessment": risk_assessment or {}
    }

    data["conversations"].append(conversation)

    # update conversation counts if present
    try:
        analytics = data.setdefault("analytics", {})
        counts = analytics.setdefault("conversation_counts", {"total_sessions": 0})
        counts["total_sessions"] = counts.get("total_sessions", 0) + 1
    except Exception:
        pass

    return conversation

def get_coping_strategies(
    data: Dict[str, Any],
    category: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Retrieve coping strategies filtered by category and/or tags. If no filters provided, returns all.
    """
    strategies = data.get("coping_strategies", [])
    if not category and not tags:
        return strategies

    def matches(s: Dict[str, Any]) -> bool:
        if category and s.get("category") != category:
            return False
        if tags:
            s_tags = set(s.get("tags", []) + s.get("suitability", []))
            if not set(tags).issubset(s_tags):
                return False
        return True

    return [s for s in strategies if matches(s)]