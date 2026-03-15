import random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()

def show_welcome():
    console.print(Panel("[bold cyan]👨‍🍳 Flavortown CLI Problem Solver v3.0[/bold cyan]", 
                  subtitle="Seu Companheiro de Programação Competitiva",
                  border_style="bright_blue"))

def show_problem(problem, current, total):
    diff_color = {"Easy": "green", "Medium": "yellow", "Hard": "red"}.get(problem.get("difficulty", "Easy"), "white")
    title = f"Questão {current}/{total} | Nível: [{diff_color}]{problem.get('difficulty', 'Normal')}[/{diff_color}]"
    console.print(Panel(f"[bold white]>{/bold white] {problem['description']}", title=title, border_style="cyan"))

def show_feedback(is_correct, answer):
    if is_correct:
        console.print("[bold green]✨ EXCELENTE! Você acertou.[/bold green]\n")
    else:
        console.print(f"[bold red]✖️ INCORRETO. Resposta: {answer}[/bold red]\n")

def ask_for_hint():
    return Confirm.ask("💡 Ativar [bold magenta]AI Assist[/bold magenta] (Gemini)?")

def show_hint(hint_text):
    console.print(Panel(f"🔍 [italic]{hint_text}[/italic]", title="Dica do Gemini", border_style="magenta"))

def show_scores(scores):
    if not scores:
        console.print("[yellow]Nenhum placar registrado.[/yellow]")
        return
    table = Table(title="🏆 Hall of Fame", border_style="bright_yellow")
    table.add_column("Hunter", justify="center", style="cyan")
    table.add_column("Points", justify="center", style="magenta")
    for score_entry in sorted(scores, key=lambda x: x.get("score", 0), reverse=True):
        table.add_row(score_entry["user"], str(score_entry["score"]))
    console.print(table)

def show_menu():
    console.print("\n[bold]1.[/bold] Iniciar Treino Local")
    console.print("[bold]2.[/bold] [bold magenta]AI Quiz Session[/bold magenta] (Gemini)")
    console.print("[bold]3.[/bold] Ver Ranking")
    console.print("[bold]4.[/bold] Sair")
    return Prompt.ask("Escolha", choices=["1", "2", "3", "4"])

def ask_theme():
    from src.ai_generator import THEMES
    console.print("\n[bold cyan]Escolha um Tema para o AI Quiz:[/bold cyan]")
    for key, val in THEMES.items():
        console.print(f"[bold]{key}.[/bold] {val}")
    return Prompt.ask("Digite o número do tema", choices=list(THEMES.keys()))
