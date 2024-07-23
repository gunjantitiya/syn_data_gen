"""Console script for syn_data_gen."""
import syn_data_gen

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for syn_data_gen."""
    console.print("Replace this message by putting your code into "
               "syn_data_gen.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
