import json
import os
from src.config import PROBLEMS_FILE

def load_problems():
    """Loads problems from the JSON file."""
    if not os.path.exists(PROBLEMS_FILE):
        return []
    
    with open(PROBLEMS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_problems(problems):
    """Saves problems to the JSON file."""
    with open(PROBLEMS_FILE, "w", encoding="utf-8") as f:
        json.dump(problems, f, indent=4, ensure_ascii=False)
