from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from schemas import RedTeamState
from engine import app

console = Console()

console.print(Panel.fit("[bold red]AI Red-Team Autonomous Security Harness[/bold red]", subtitle="Multi-Agent Adversarial Test"))

initial_state = RedTeamState(max_rounds=2)
final_state = app.invoke(initial_state)

table = Table(title="Execution Summary & Adversarial Audit")
table.add_column("Round", style="cyan", justify="center")
table.add_column("Attack Vector", style="magenta")
table.add_column("Prompt Extract", style="white")
table.add_column("Breached?", justify="center")
table.add_column("Severity (1-10)", justify="center")

for log in final_state["attack_logs"]:
    status = "[bold red]FAIL (LEAKED)[/bold red]" if log["compromised"] else "[bold green]PASS (BLOCKED)[/bold green]"
    table.add_row(
        str(log["round"]),
        log["attack_type"],
        log["prompt"][:40] + "...",
        status,
        str(log["severity"])
    )

console.print(table)
