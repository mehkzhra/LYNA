import json
import os

CASES_FILE = os.path.join(os.path.dirname(__file__), "..", "cases.json")

def load_cases():
    with open(CASES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

CASES = load_cases()

def get_case(case_id: str):
    for c in CASES:
        if c["id"] == case_id:
            return c
    return None
