import json

def extract_qa(data):
    qa_pairs = {}

    # College info
    college = data.get("college", {})
    if college:
        qa_pairs["What is the full name of RJIT?"] = college.get("name", "")
        qa_pairs["What is RJIT's short name?"] = college.get("short_name", "")
        qa_pairs["Where is RJIT located?"] = college.get("location", "")
        qa_pairs["When was RJIT established?"] = str(college.get("established", ""))
        qa_pairs["What is RJIT affiliated to?"] = college.get("affiliation", "")
        qa_pairs["What is RJIT's official website?"] = college.get("website", "")

    # Admissions - Undergraduate
    ug = data.get("admissions", {}).get("undergraduate", {})
    if ug:
        qa_pairs["Which undergraduate courses are offered?"] = ", ".join(ug.get("courses", []))
        qa_pairs["What is the eligibility for undergraduate admissions?"] = ug.get("eligibility", "")
        fee = ug.get("fee_structure", {})
        qa_pairs["What is the first year fee for undergraduate courses?"] = fee.get("first_year", "")
        qa_pairs["What is the total fee for undergraduate courses?"] = fee.get("total", "")
        dates = ug.get("important_dates", {})
        for key, value in dates.items():
            qa_pairs[f"When is the {key.replace('_', ' ')}?"] = value

    # Admissions - Postgraduate
    pg = data.get("admissions", {}).get("postgraduate", {})
    if pg:
        qa_pairs["Which postgraduate courses are offered?"] = ", ".join(pg.get("courses", []))
        qa_pairs["What is the eligibility for postgraduate admissions?"] = pg.get("eligibility", "")
        fee = pg.get("fee_structure", {})
        qa_pairs["What is the first year fee for postgraduate courses?"] = fee.get("first_year", "")
        qa_pairs["What is the total fee for postgraduate courses?"] = fee.get("total", "")

    # Infrastructure - Campus buildings and facilities
    campus = data.get("infrastructure", {}).get("campus", {})
    if campus:
        qa_pairs["What are the main buildings in the RJIT campus?"] = ", ".join(campus.get("buildings", []))
        qa_pairs["What facilities does RJIT campus provide?"] = ", ".join(campus.get("facilities", []))

    # Labs
    labs = data.get("infrastructure", {}).get("labs", [])
    if labs:
        qa_pairs["Which labs are available at RJIT?"] = ", ".join(labs)

    # Departments
    departments = data.get("departments", [])
    if departments:
        dept_names = [dept.get("name", "") for dept in departments]
        qa_pairs["Which departments are available at RJIT?"] = ", ".join(dept_names)
        for dept in departments:
            qa_pairs[f"Who is the HOD of {dept.get('name', '')}?"] = dept.get("hod", "")

    # Hostel
    hostel = data.get("hostel", {})
    if hostel:
        qa_pairs["What hostel facilities are provided?"] = ", ".join(hostel.get("facilities", []))
        fees = hostel.get("fees", {})
        for key, value in fees.items():
            qa_pairs[f"What is the {key.replace('_', ' ')} fee?"] = value

    # Events - annual fest and recent events
    events = data.get("events", {})
    annual = events.get("annual_fest", {})
    if annual:
        qa_pairs["What is the name of RJIT's annual fest?"] = annual.get("name", "")
        qa_pairs["Describe the annual fest."] = annual.get("description", "")
        latest = annual.get("latest_event", {})
        if latest:
            qa_pairs[f"What was the latest event in the annual fest {annual.get('name', '')}?"] = f"{latest.get('name', '')} on {latest.get('date', '')}: {latest.get('description', '')}"

    recent_events = events.get("recent_events", [])
    for event in recent_events:
        question = f"Tell me about the event {event.get('name', '')}."
        answer = f"Date: {event.get('date', '')}. Description: {event.get('description', '')}."
        qa_pairs[question] = answer

    # News
    news_list = data.get("news", [])
    for news in news_list:
        question = f"What is the news titled '{news.get('title', '')}'?"
        answer = f"Date: {news.get('date', '')}. More info: {news.get('link', '')}"
        qa_pairs[question] = answer

    # Sports
    sports = data.get("sports", {})
    if sports:
        qa_pairs["What sports facilities are available?"] = ", ".join(sports.get("facilities", []))
        clubs = sports.get("clubs", [])
        qa_pairs["What sports clubs exist at RJIT?"] = ", ".join(clubs)

    # Clubs
    clubs = data.get("clubs", [])
    for club in clubs:
        question = f"Tell me about the club {club.get('name', '')}."
        description = club.get("description", "")
        socials = club.get("social_media", {})
        social_links = ", ".join(socials.values())
        answer = f"{description}. Social media: {social_links}"
        qa_pairs[question] = answer

    # Faculty
    faculty = data.get("faculty", {})
    for role, info in faculty.items():
        qa_pairs[f"Who is the {role.upper()} of RJIT?"] = info.get("name", "")

    return qa_pairs

# Load original big JSON file
with open("rjit_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

qa = extract_qa(data)

# Save flattened Q-A JSON
with open("rjit_qa.json", "w", encoding="utf-8") as f:
    json.dump(qa, f, indent=2, ensure_ascii=False)

print("✅ Extracted question-answer pairs saved to rjit_qa.json")
