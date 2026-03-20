import json
import os
from typing import List, Dict

# Temas disponíveis
THEMES = {
    "1": "Estruturas de Dados",
    "2": "Algoritmos",
    "3": "Banco de Dados",
    "4": "Redes de Computadores",
    "5": "Sistemas Operacionais"
}

def generate_ai_problems(theme_id: str) -> List[Dict]:
    """Gera problemas com IA. Se falhar ou não houver lib, usa Mock Mode."""
    theme = THEMES.get(theme_id, "Programação Geral")
    api_key = os.environ.get("GOOGLE_API_KEY", "")

    # Tenta importar a biblioteca apenas quando for usar
    try:
        import google.generativeai as genai
        has_lib = True
    except ImportError:
        has_lib = False

    # Se não tiver a chave ou não tiver a biblioteca, usa o Mock Mode Profissional
    if not api_key or not has_lib:
        return [
            {
                "id": f"ai-mock-{i}",
                "description": f"[MOCK] Qual é o conceito principal de {theme} aplicado no cenário {i}?",
                "answer": "Abstração",
                "difficulty": "Medium",
                "hint": "Pense em simplificação de sistemas."
            } for i in range(1, 6)
        ]

    # Se chegou aqui, tem a lib e a chave. Usa o Gemini real!
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Gere 5 perguntas curtas (1-2 linhas) sobre {theme} em JSON: [{{id, description, answer, difficulty, hint}}]"
        
        response = model.generate_content(
            prompt, 
            generation_config=genai.GenerationConfig(response_mime_type="application/json")
        )
        return json.loads(response.text)
    except Exception:
        # Fallback de segurança
        return [{"id": "err", "description": "Erro na API. Use o modo local.", "answer": "-", "difficulty": "Easy", "hint": "Tente novamente."}]
