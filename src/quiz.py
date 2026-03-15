import random
from src import ui, problems, scoring
from src.ai_generator import generate_ai_problems

QUESTIONS_PER_SESSION = 5

def run_quiz(session_problems=None):
    if session_problems is None:
        all_problems = problems.load_problems()
        if not all_problems or len(all_problems) < QUESTIONS_PER_SESSION:
            ui.console.print("[bold red]Banco de dados insuficiente![/bold red]")
            return
        session_problems = random.sample(all_problems, QUESTIONS_PER_SESSION)
    
    score = 0
    ui.console.print(f"\n[bold cyan]🏁 Iniciando sessão v3.0 com {len(session_problems)} questões...[/bold cyan]\n")
    
    for i, problem in enumerate(session_problems, 1):
        ui.show_problem(problem, current=i, total=len(session_problems))
        user_answer = ui.Prompt.ask("Resposta").strip().lower()
        correct_answer = str(problem['answer']).strip().lower()
        is_correct = user_answer == correct_answer
        
        if not is_correct and problem.get('hint') and ui.ask_for_hint():
            ui.show_hint(problem['hint'])
            user_answer = ui.Prompt.ask("Tente novamente").strip().lower()
            is_correct = user_answer == correct_answer
        
        ui.show_feedback(is_correct, problem['answer'])
        if is_correct: score += 1
            
    ui.console.print(f"[bold]Sessão encerrada![/bold] Score: [bold green]{score}/{len(session_problems)}[/bold green].")
    if score > 0:
        user_name = ui.Prompt.ask("Nick (Enter p/ pular)", default="")
        if user_name: scoring.save_score(user_name, score)

def run_ai_quiz():
    theme_id = ui.ask_theme()
    with ui.console.status("[bold magenta]IA está gerando suas questões...[/bold magenta]"):
        ai_problems = generate_ai_problems(theme_id)
    if not ai_problems:
        ui.console.print("[bold red]Falha ao gerar problemas com IA.[/bold red]")
        return
    run_quiz(ai_problems)

def main_loop():
    ui.show_welcome()
    while True:
        choice = ui.show_menu()
        if choice == "1": run_quiz()
        elif choice == "2": run_ai_quiz()
        elif choice == "3": ui.show_scores(scoring.load_scores())
        elif choice == "4": break
