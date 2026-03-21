import json
import os
import urllib.request
from typing import List, Dict

# Available Themes
THEMES = {
    "1": "Data Structures",
    "2": "Algorithms",
    "3": "Databases",
    "4": "Computer Networks",
    "5": "Operating Systems"
}

def call_gemini_api(prompt: str, is_json: bool = True) -> str:
    """Calls Gemini API via REST (no heavy dependencies)."""
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key:
        return ""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    if is_json:
        data["generationConfig"] = {"response_mime_type": "application/json"}

    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        # Silently fail to Mock Mode
        return ""

def generate_ai_problems(theme_id: str) -> List[Dict]:
    """Generates problems using Gemini REST API."""
    theme = THEMES.get(theme_id, "General Programming")
    
    prompt = (
        f"Generate 5 short technical questions about {theme}. "
        "Return ONLY a JSON array with these fields: "
        "id (int), description (string), answer (short string), difficulty (Easy/Medium/Hard), hint (string)."
    )

    response_text = call_gemini_api(prompt, is_json=True)
    
    if response_text:
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            pass

    # Professional Mock Mode (Fallback if API fails or No Key)
    return [
        {
            "id": i,
            "description": f"[MOCK] What is the core principle of {theme} regarding scalability?",
            "answer": "Modularity",
            "difficulty": "Medium",
            "hint": "Think about 'divide and conquer'."
        } for i in range(1, 6)
    ]

def get_ai_explanation(question: str, user_answer: str, correct_answer: str) -> str:
    """Generates a dynamic explanation for the user's mistake."""
    prompt = (
        f"A student missed this question: '{question}'. "
        f"They answered '{user_answer}', but the correct answer was '{correct_answer}'. "
        "Explain in a very short, friendly way (max 2 lines) why the correct answer is right."
    )
    explanation = call_gemini_api(prompt, is_json=False)
    return explanation if explanation else f"Don't worry! Keep studying {correct_answer} concepts."
