from datetime import datetime

def get_today_events_url():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    return f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{today}"


def extract_finished_matches(payload):
    finished = []

    for event in payload.get("events", []):
        if event.get("status", {}).get("type") == "finished":
            finished.append({
                "match_id": event["id"],
                "home": event["homeTeam"]["name"],
                "away": event["awayTeam"]["name"],
                "timestamp": event.get("endTimestamp"),
            })

    return finished
