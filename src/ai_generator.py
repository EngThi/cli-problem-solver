import json
import os
import urllib.request
from typing import List, Dict, Optional

# Available Themes
THEMES = {
    "1": "Data Structures & Memory Management",
    "2": "Advanced Algorithms & Optimization",
    "3": "Distributed Systems & Databases",
    "4": "Network Protocols & Security",
    "5": "Kernel & Operating Systems"
}

def call_gemini_api(prompt: str, is_json: bool = True) -> Optional[str]:
    """Calls Gemini 3.1 Flash Lite Preview via REST API."""
    # Using environment variable for security
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key:
        return None

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    
    system_instruction = (
        "You are an Elite Staff Engineer. Provide deep technical content. "
        "Return ONLY the requested format (JSON array or short explanation)."
    )
    
    data = {
        "contents": [{"parts": [{"text": f"{system_instruction}\n\nUser Request: {prompt}"}]}]
    }
    
    if is_json:
        data["generationConfig"] = {"response_mime_type": "application/json"}

    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            text = result['candidates'][0]['content']['parts'][0]['text']
            if is_json:
                text = text.replace("```json", "").replace("```", "").strip()
            return text
    except Exception:
        return None

def generate_ai_problems(theme_id: str) -> Optional[List[Dict]]:
    """Generates 5 distinct problems via AI. Returns None on failure."""
    theme = THEMES.get(theme_id, "System Design")
    
    prompt = (
        f"Generate 5 distinct, high-level technical challenges about {theme}. "
        "Context: Real-world scenarios at Big Tech companies. "
        "Format: JSON array of objects {id (G3-UUID), description, answer, difficulty, hint}."
    )

    response_text = call_gemini_api(prompt, is_json=True)
    if response_text:
        try:
            return json.loads(response_text)
        except:
            return None
    return None

def get_ai_explanation(question: str, user_answer: str, correct_answer: str) -> Optional[str]:
    """AI-powered conceptual gap analysis."""
    prompt = (
        f"The user failed this question: '{question}'. "
        f"They answered '{user_answer}', but the correct answer is '{correct_answer}'. "
        "Explain the conceptual gap in 2 lines."
    )
    return call_gemini_api(prompt, is_json=False)
