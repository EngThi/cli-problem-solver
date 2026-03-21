import json
import os
from src.config import SCORES_FILE

def load_scores():
    """Loads the scoring history."""
    if not os.path.exists(SCORES_FILE):
        return []
    
    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_score(user_name, score):
    """Saves a new score to the history."""
    scores = load_scores()
    scores.append({
        "user": user_name,
        "score": score,
        "timestamp": os.path.getmtime(SCORES_FILE) if os.path.exists(SCORES_FILE) else None
    })
    
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=4, ensure_ascii=False)
