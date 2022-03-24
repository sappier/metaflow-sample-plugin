from metaflow._vendor import click
from metaflow import parameters


@click.group()
def cli():
    pass


@parameters.add_custom_parameters(deploy_mode=False)
@cli.command(help="Sample metaflow plugin cli command.")
@click.option("--debug/--no-debug", default=False)
@click.pass_obj
def sample(obj, debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")
