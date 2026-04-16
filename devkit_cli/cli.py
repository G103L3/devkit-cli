import click


@click.group(invoke_without_command=True, context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(package_name='devkit-cli')
def cli():
    """devkit-cli: A developer toolkit command-line interface."""
    pass


@cli.command()
def hello():
    """Print a friendly greeting."""
    click.echo("Hello from devkit-cli! 🛠️")


if __name__ == "__main__":
    cli()