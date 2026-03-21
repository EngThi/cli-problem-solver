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

def show_problem(problem, current, total, is_ai=False):
    diff_color = {"Easy": "green", "Medium": "yellow", "Hard": "red"}.get(problem.get("difficulty", "Easy"), "white")
    
    if is_ai:
        # Visual de IA: Bordas Neon, Título de Agente
        title = f"🤖 [bold magenta]SYSTEM.BRAIN_ENGINE v3.0[/bold magenta] | Questão {current}/{total} | {problem.get('id', 'AI-X')}"
        border = "magenta"
        prefix = "[bold magenta]AI-PROMPT>[/bold magenta] "
    else:
        # Visual Local: Bordas Cyan
        title = f"📁 [bold cyan]LOCAL.STORAGE[/bold cyan] | Questão {current}/{total} | ID: {problem.get('id', '?')}"
        border = "cyan"
        prefix = "[bold cyan]LOCAL-DB>[/bold cyan] "

    # Corrigido: Removido as chaves de {/dim} que causavam o NameError
    content = f"{prefix}{problem['description']}\n\n[dim]Difficulty:[/dim] [{diff_color}]{problem.get('difficulty', 'Normal')}[/{diff_color}]"
    console.print(Panel(content, title=title, border_style=border))

def show_feedback(is_correct, answer):
    if is_correct:
        console.print("[bold green]✨ EXCELENTE! Você acertou.[/bold green]\n")
    else:
        console.print(f"[bold red]✖️ INCORRETO. Raciocínio esperado: {answer}[/bold red]\n")

def ask_for_hint():
    return Confirm.ask("💡 Ativar [bold magenta]AI Assist[/bold magenta] (Análise em tempo real do Gemini)?")

def show_hint(hint_text):
    console.print(Panel(f"🧠 [italic magenta]{hint_text}[/italic magenta]", 
                        title="[bold magenta]GEMINI 3.0 FLASH PREVIEW ANALYSIS[/bold magenta]", 
                        border_style="magenta"))

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
    console.print("\n[bold white]ESCOLHA SEU MODO DE COMANDO:[/bold white]")
    console.print("[bold cyan]1.[/bold cyan] Treino Local (Base Estática)")
    console.print("[bold magenta]2. AI Quiz Session (Gemini 3.0 Flash Preview)[/bold magenta]")
    console.print("[bold cyan]3.[/bold cyan] Ver Ranking")
    console.print("[bold cyan]4.[/bold cyan] Sair")
    return Prompt.ask("Escolha", choices=["1", "2", "3", "4"])

def ask_theme():
    from src.ai_generator import THEMES
    console.print("\n[bold cyan]Selecione o domínio para a Geração de IA:[/bold cyan]")
    for key, val in THEMES.items():
        console.print(f"[bold magenta]{key}.[/bold magenta] {val}")
    return Prompt.ask("Domínio", choices=list(THEMES.keys()))
