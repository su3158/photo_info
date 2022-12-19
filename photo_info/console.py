from rich.console import Console
from rich.table import Table

console = Console()


def test():
    console.print("Hello", "World", style="bold red")


def test_table():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Production Budget", justify="right")
    table.add_column("Box Office", justify="right")
    table.add_row(
        "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
    )

    console.print(table)


def echo(text):
    console.print(text, style="bold red")


def table(datas):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    for data in datas:
        table.add_row(data)

    console.print(table)
