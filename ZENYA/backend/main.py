from flask import Flask, jsonify, request, send_from_directory
from datetime import datetime
import json
import os

app = Flask(__name__, static_folder="../frontend/assets", template_folder="../frontend")

USER_DATA_FILE = "backend/user_data.json"

# ---------------------------
# Utility Functions
# ---------------------------
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {"moods": [], "conversations": []}


def save_user_data(data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------------
# API Endpoints
# ---------------------------
@app.route("/add-mood", methods=["POST"])
def add_mood():
    data = load_user_data()
    mood = request.json.get("mood")
    entry = {"mood": mood, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    data["moods"].append(entry)
    save_user_data(data)
    return jsonify({"status": "success", "message": "Mood added successfully!"})


@app.route("/add-conv", methods=["POST"])
def add_conversation():
    data = load_user_data()
    conv = request.json.get("conversation")
    entry = {"conversation": conv, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    data["conversations"].append(entry)
    save_user_data(data)
    return jsonify({"status": "success", "message": "Conversation saved!"})


# ---------------------------
# Serve Frontend
# ---------------------------
@app.route("/")
def serve_index():
    return send_from_directory("../frontend", "index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    # Serve assets (JS, CSS, images, etc.)
    if os.path.exists(os.path.join("../frontend/assets", filename)):
        return send_from_directory("../frontend/assets", filename)
    elif os.path.exists(os.path.join("../frontend", filename)):
        return send_from_directory("../frontend", filename)
    else:
        return "File not found", 404


# ---------------------------
# Run Server
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
