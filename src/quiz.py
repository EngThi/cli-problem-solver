import random
from src import ui, problems, scoring
from src.ai_generator import generate_ai_problems, get_ai_explanation

QUESTIONS_PER_SESSION = 5

def run_quiz(session_problems=None, is_ai=False):
    if session_problems is None:
        all_problems = problems.load_problems()
        if not all_problems or len(all_problems) < QUESTIONS_PER_SESSION:
            ui.console.print("[bold red]ERROR: Local Database not found![/bold red]")
            return
        session_problems = random.sample(all_problems, QUESTIONS_PER_SESSION)
    
    score = 0
    ui.console.print(f"\n[bold cyan]🏁 Session Initialized: {'AI ENGINE' if is_ai else 'LOCAL DB'}[/bold cyan]\n")
    
    for i, problem in enumerate(session_problems, 1):
        ui.show_problem(problem, current=i, total=len(session_problems), is_ai=is_ai)
        
        user_answer = ui.Prompt.ask("ENTRADA").strip().lower()
        correct_answer = str(problem['answer']).strip().lower()
        is_correct = user_answer == correct_answer
        
        if not is_correct and ui.ask_for_hint():
            with ui.console.status("[bold magenta]🛰️ ANALYZING...[/bold magenta]"):
                explanation = get_ai_explanation(
                    problem['description'], 
                    user_answer, 
                    problem['answer']
                )
            if explanation:
                ui.show_hint(explanation)
                user_answer = ui.Prompt.ask("RE-TRY ENTRADA").strip().lower()
                is_correct = user_answer == correct_answer
            else:
                ui.console.print("[bold red]SYSTEM.BRAIN_ENGINE: OFFLINE. Check connection or API Key.[/bold red]")
        
        ui.show_feedback(is_correct, problem['answer'])
        if is_correct: score += 1
            
    ui.console.print(f"[bold]Session Ended.[/bold] Final Score: [bold green]{score}/{len(session_problems)}[/bold green].")
    if score > 0:
        user_name = ui.Prompt.ask("NICKNAME", default="")
        if user_name: scoring.save_score(user_name, score)

def run_ai_quiz():
    theme_id = ui.ask_theme()
    with ui.console.status("[bold magenta]🛰️ CONNECTING TO BRAIN ENGINE...[/bold magenta]"):
        ai_problems = generate_ai_problems(theme_id)
    
    if not ai_problems:
        ui.console.print("\n[bold red]CRITICAL ERROR: CONNECTION FAILED[/bold red]")
        ui.console.print("[yellow]Please check if GOOGLE_API_KEY is exported or if you have internet access.[/yellow]")
        return
        
    run_quiz(ai_problems, is_ai=True)

def main_loop():
    ui.show_welcome()
    while True:
        choice = ui.show_menu()
        if choice == "1": run_quiz(is_ai=False)
        elif choice == "2": run_ai_quiz()
        elif choice == "3": ui.show_scores(scoring.load_scores())
        elif choice == "4": break
