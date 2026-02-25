from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def show_welcome():
    console.print(Panel("[bold cyan]👨‍🍳 Flavortown CLI Problem Solver v2.0[/bold cyan]", subtitle="Powered by Rich CLI"))

def show_problem(problem):
    console.print(Panel(f"[bold yellow]PERGUNTA:[/bold yellow] {problem['description']}", title=f"Problema ID: {problem.get('id', 'N/A')}"))

def show_feedback(is_correct, answer):
    if is_correct:
        console.print("[bold green]✅ ACERTOU! Mandou bem chef![/bold green]")
    else:
        console.print(f"[bold red]❌ ERROU! A resposta era: {answer}[/bold red]")

def show_scores(scores):
    if not scores:
        console.print("[yellow]Nenhum placar registrado ainda.[/yellow]")
        return
    
    table = Table(title="🏆 Ranking de Pontuações")
    table.add_column("Jogador", justify="center", style="cyan", no_wrap=True)
    table.add_column("Pontuação", justify="center", style="magenta")
    
    for score_entry in scores:
        table.add_row(score_entry["user"], str(score_entry["score"]))
    
    console.print(table)

def show_menu():
    console.print("\n[bold]1.[/bold] Resolver um problema")
    console.print("[bold]2.[/bold] Ver ranking")
    console.print("[bold]3.[/bold] Sair")
    return Prompt.ask("Escolha", choices=["1", "2", "3"])
