import click


@click.group()
def cli():
    """devkit-cli: A developer toolkit command-line interface."""
    pass


@cli.command()
def hello():
    """Print a friendly greeting."""
    click.echo("Hello from devkit-cli! 🛠️")


if __name__ == "__main__":
    cli()