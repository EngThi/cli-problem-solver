import random
from src import ui, problems, scoring
from src.ai_generator import generate_ai_problems, get_ai_explanation

QUESTIONS_PER_SESSION = 5

def run_quiz(session_problems=None):
    if session_problems is None:
        all_problems = problems.load_problems()
        if not all_problems or len(all_problems) < QUESTIONS_PER_SESSION:
            ui.console.print("[bold red]Insufficient problem database![/bold red]")
            return
        session_problems = random.sample(all_problems, QUESTIONS_PER_SESSION)
    
    score = 0
    ui.console.print(f"\n[bold cyan]🏁 Starting session v3.0 with {len(session_problems)} questions...[/bold cyan]\n")
    
    for i, problem in enumerate(session_problems, 1):
        ui.show_problem(problem, current=i, total=len(session_problems))
        user_answer = ui.Prompt.ask("Your Answer").strip().lower()
        correct_answer = str(problem['answer']).strip().lower()
        is_correct = user_answer == correct_answer
        
        # First attempt with static hint
        if not is_correct and problem.get('hint') and ui.ask_for_hint():
            ui.show_hint(problem['hint'])
            user_answer = ui.Prompt.ask("Try again").strip().lower()
            is_correct = user_answer == correct_answer
        
        # Final feedback
        ui.show_feedback(is_correct, problem['answer'])
        
        # Dynamic AI explanation on failure
        if not is_correct:
            if ui.Confirm.ask("🤔 Want the [bold magenta]AI[/bold magenta] to explain why you missed it?"):
                with ui.console.status("[bold magenta]AI is analyzing your mistake...[/bold magenta]"):
                    explanation = get_ai_explanation(problem['description'], user_answer, problem['answer'])
                ui.show_hint(explanation)

        if is_correct: score += 1
            
    ui.console.print(f"[bold]Session Complete![/bold] Final Score: [bold green]{score}/{len(session_problems)}[/bold green].")
    if score > 0:
        user_name = ui.Prompt.ask("Enter your Nickname (Enter to skip)", default="")
        if user_name: scoring.save_score(user_name, score)

def run_ai_quiz():
    theme_id = ui.ask_theme()
    with ui.console.status("[bold magenta]AI is cooking up your questions...[/bold magenta]"):
        ai_problems = generate_ai_problems(theme_id)
    if not ai_problems:
        ui.console.print("[bold red]Failed to generate AI problems.[/bold red]")
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
