import random
import json
import os

def carregar_problemas():
    if not os.path.exists('problems.json'):
        print("⚠️  Arquivo 'problems.json' não encontrado!")
        return []
    
    with open('problems.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("--- FLAVORTOWN NIBBLE QUIZ ---")
    problemas = carregar_problemas()
    
    if not problemas:
        print("Nenhum problema carregado. Verifique o arquivo JSON.")
        return

    while True:
        print("\n1. Resolver um problema")
        print("2. Sair")
        
        # Validação de input (Paranoia Saudável)
        escolha = input("Escolha (1/2): ")
        
        if escolha == "1":
            # Lógica de Sorteio
            problema = random.choice(problemas)
            
            print(f"\n[ID: {problema.get('id', '?')}]")
            print(f"PERGUNTA: {problema['description']}")
            
            resposta_user = input("Sua resposta: ").strip()
            
            # Comparação (case-insensitive)
            if resposta_user.lower() == problema['answer'].lower():
                print("✅ ACERTOU! Mandou bem chef!")
            else:
                print(f"❌ ERROU! A resposta era: {problema['answer']}")
                
        elif escolha == "2":
            print("Saindo da cozinha...")
            break
        else:
            print("Opção inválida. Tente de novo.")

# O ponto de entrada do Python
if __name__ == "__main__":
    main()
