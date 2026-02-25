import random
from src import ui
from src import problems
from src import scoring

def run_quiz():
    all_problems = problems.load_problems()
    if not all_problems:
        ui.console.print("[bold red]Nenhum problema encontrado no banco![/bold red]")
        return
    
    problem = random.choice(all_problems)
    ui.show_problem(problem)
    
    user_answer = ui.Prompt.ask("Sua resposta").strip().lower()
    correct_answer = problem['answer'].strip().lower()
    
    is_correct = user_answer == correct_answer
    ui.show_feedback(is_correct, problem['answer'])
    
    if is_correct:
        # Por agora só salva 1 ponto, podemos melhorar
        user_name = ui.Prompt.ask("Seu nome para o ranking")
        scoring.save_score(user_name, 1)

def main_loop():
    ui.show_welcome()
    while True:
        choice = ui.show_menu()
        if choice == "1":
            run_quiz()
        elif choice == "2":
            scores = scoring.load_scores()
            ui.show_scores(scores)
        elif choice == "3":
            ui.console.print("[yellow]Saindo da cozinha... 🧑🏽‍🍳[/yellow]")
            break
