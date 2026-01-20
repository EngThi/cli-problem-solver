import random

# 1. DADOS (O "Banco de Dados" na memória)
# Lista de dicionários. Cada {} é um problema.
problemas = [
    {
        "pergunta": "Quanto é 15 + 15?",
        "resposta": "30",  # String para evitar erro de tipo
        "dificuldade": "Facil"
    },
    {
        "pergunta": "Qual a linguagem de cobra?",
        "resposta": "python",
        "dificuldade": "Facil"
    },
    {
        "pergunta": "O que significa CPU?",
        "resposta": "processador",
        "dificuldade": "Medio"
    }
]

def main():
    print("--- FLAVORTOWN NIBBLE QUIZ ---")
    print("1. Resolver um problema")
    print("2. Sair")
    
    # Validação de input (Paranoia Saudável)
    escolha = input("Escolha (1/2): ")
    
    if escolha == "1":
        # Lógica de Sorteio
        problema = random.choice(problemas)
        
        print(f"\n[Nível: {problema['dificuldade']}]")
        print(f"PERGUNTA: {problema['pergunta']}")
        
        resposta_user = input("Sua resposta: ").lower().strip() # .lower() ignora maiúsculas
        
        # Comparação
        if resposta_user == problema['resposta']:
            print("✅ ACERTOU! Mandou bem chef!")
        else:
            print(f"❌ ERROU! A resposta era: {problema['resposta']}")
            
    elif escolha == "2":
        print("Saindo da cozinha...")
    else:
        print("Opção inválida. Tente de novo.")

# O ponto de entrada do Python
if __name__ == "__main__":
    main()