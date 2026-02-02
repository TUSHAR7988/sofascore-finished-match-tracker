# import json
# import os
# from datetime import datetime

# OUTPUT_DIR = "output"

# os.makedirs(OUTPUT_DIR, exist_ok=True)

# def write_match_json(match):
#     """
#     Writes one JSON file per finished match.
#     Filename = <match_id>.json
#     """

#     match_id = match["match_id"]
#     filepath = os.path.join(OUTPUT_DIR, f"{match_id}.json")

#     payload = {
#         "match_id": match_id,
#         "home_team": match["home"],
#         "away_team": match["away"],
#         "timestamp": match["timestamp"],
#         "status": "finished",
#         "scraped_at": datetime.utcnow().isoformat() + "Z"
#     }

#     with open(filepath, "w", encoding="utf-8") as f:
#         json.dump(payload, f, ensure_ascii=False, indent=2)


import json
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def write_match_json(match):
    path = OUTPUT_DIR / f"{match['match_id']}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(match, f, ensure_ascii=False, indent=2)
