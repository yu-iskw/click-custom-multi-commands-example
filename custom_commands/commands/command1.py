import click


@click.group()
def cli():
    """The sub root of this commands."""
    pass


@cli.command()
def create():
    click.echo('create is invoked in command1.')


@cli.command()
def delete():
    click.echo('delete is invoked in command1.')


@cli.command()
def update():
    click.echo('update is invoked in command1.')
