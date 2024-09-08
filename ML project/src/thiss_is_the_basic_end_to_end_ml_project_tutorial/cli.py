"""Console script for thiss_is_the_basic_end_to_end_ml_project_tutorial."""
import thiss_is_the_basic_end_to_end_ml_project_tutorial

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for thiss_is_the_basic_end_to_end_ml_project_tutorial."""
    console.print("Replace this message by putting your code into "
               "thiss_is_the_basic_end_to_end_ml_project_tutorial.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
