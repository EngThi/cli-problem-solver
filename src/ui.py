from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()

def show_welcome():
    console.print(Panel("[bold cyan]👨‍🍳 Flavortown CLI Problem Solver v3.0[/bold cyan]", subtitle="Powered by Rich & AI"))

def show_problem(problem, current, total):
    diff_color = {"Easy": "green", "Medium": "yellow", "Hard": "red"}.get(problem.get("difficulty", "Easy"), "white")
    
    title = f"Questão {current}/{total} | ID: {problem.get('id', '?')} | Nível: [{diff_color}]{problem.get('difficulty', 'Normal')}[/{diff_color}]"
    console.print(Panel(f"[bold yellow]PERGUNTA:[/bold yellow] {problem['description']}", title=title))

def show_feedback(is_correct, answer):
    if is_correct:
        console.print("[bold green]✅ ACERTOU! Mandou bem chef![/bold green]\n")
    else:
        console.print(f"[bold red]❌ ERROU! A resposta esperada era: {answer}[/bold red]\n")

def ask_for_hint():
    return Confirm.ask("💡 Quer usar o [bold magenta]AI Hint[/bold magenta] (Dica do Gemini)?")

def show_hint(hint_text):
    console.print(Panel(f"🧠 [italic magenta]{hint_text}[/italic magenta]", title="🤖 Gemini Hint", border_style="magenta"))

def show_scores(scores):
    if not scores:
        console.print("[yellow]Nenhum placar registrado ainda.[/yellow]")
        return
    
    table = Table(title="🏆 Ranking de Pontuações")
    table.add_column("Jogador", justify="center", style="cyan", no_wrap=True)
    table.add_column("Pontuação", justify="center", style="magenta")
    
    # Ordenar por pontuação decrescente
    sorted_scores = sorted(scores, key=lambda x: x.get("score", 0), reverse=True)
    for score_entry in sorted_scores:
        table.add_row(score_entry["user"], str(score_entry["score"]))
    
    console.print(table)

def show_menu():
    console.print("\n[bold]1.[/bold] Iniciar Sessão de Treino (5 Perguntas)")
    console.print("[bold]2.[/bold] Ver Ranking")
    console.print("[bold]3.[/bold] Sair")
    return Prompt.ask("Escolha", choices=["1", "2", "3"])
