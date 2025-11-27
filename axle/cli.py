import click


@click.group()
def cli():
    pass


@cli.command(help="List all available templates")
def list():
    click.echo("Listing templates...")


@cli.command(help="Use this to store a template")
def store():
    click.echo("Keeping template...")


@cli.command(help="Use this to permanently delete a template")
def remove():
    click.echo("Deleting template...")


def main():
    cli()


if __name__ == "__main__":
    main()
