import random
from src import ui
from src import problems
from src import scoring

QUESTIONS_PER_SESSION = 5

def run_quiz():
    all_problems = problems.load_problems()
    if not all_problems or len(all_problems) < QUESTIONS_PER_SESSION:
        ui.console.print("[bold red]Problemas insuficientes no banco![/bold red]")
        return
    
    # Seleciona 5 perguntas aleatórias sem repetir
    session_problems = random.sample(all_problems, QUESTIONS_PER_SESSION)
    score = 0
    
    ui.console.print(f"\n[bold cyan]🏁 Iniciando sessão de treino com {QUESTIONS_PER_SESSION} questões...[/bold cyan]\n")
    
    for i, problem in enumerate(session_problems, 1):
        ui.show_problem(problem, current=i, total=QUESTIONS_PER_SESSION)
        
        user_answer = ui.Prompt.ask("Sua resposta").strip().lower()
        correct_answer = problem['answer'].strip().lower()
        
        is_correct = user_answer == correct_answer
        
        # Lógica de Erro + IA Hint
        if not is_correct:
            if problem.get('hint') and ui.ask_for_hint():
                ui.show_hint(problem['hint'])
                # Segunda chance
                user_answer = ui.Prompt.ask("Tente novamente").strip().lower()
                is_correct = user_answer == correct_answer
        
        ui.show_feedback(is_correct, problem['answer'])
        
        if is_correct:
            score += 1
            
    # Fim da Sessão
    ui.console.print(f"[bold]Sessão encerrada![/bold] Você acertou [bold green]{score}/{QUESTIONS_PER_SESSION}[/bold green].")
    
    if score > 0:
        user_name = ui.Prompt.ask("Seu nome para o ranking (Enter para pular)", default="")
        if user_name:
            scoring.save_score(user_name, score)

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
            ui.console.print("[yellow]Saindo do terminal... Até a próxima! 🧑🏽‍💻[/yellow]")
            break
