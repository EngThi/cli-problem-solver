import json, os, google.generativeai as genai
api_key = os.environ.get("GOOGLE_API_KEY", "")
THEMES = {"1": "Estruturas de Dados", "2": "Algoritmos", "3": "Banco de Dados", "4": "Redes", "5": "Sistemas Operacionais"}
def generate_ai_problems(theme_id: str):
    theme = THEMES.get(theme_id, "Geral")
    if not api_key: return [{"id": f"AI-{i}", "description": f"Questão {theme} {i}", "answer": "Resposta", "difficulty": "Medium", "hint": "Dica"} for i in range(1, 6)]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        res = model.generate_content(f"Gere 5 questões sobre {theme} em JSON: [{{id, description, answer, difficulty, hint}}]", generation_config=genai.GenerationConfig(response_mime_type="application/json"))
        return json.loads(res.text)
    except: return []
