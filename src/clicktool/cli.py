"""
Main entrypoint for the CLI
"""

import click


@click.group(help='Clicktool dummmy CLI, it really does NOTHING')
@click.version_option()
def cli():
    """ Entry point to CLI options."""
    pass  # do nothing here, it just defines the name for other subcommands


@cli.command(name='ls', help='List, again dummy')
@click.option('--all', '-a', is_flag=True)
@click.option('--path', '-p', required=False)
def ls(all, path):
    """ This should do `ls`. """
    to_echo = "ls"
    if all:
        to_echo = f'{to_echo} --all'
    if path:
        to_echo = f'{to_echo} --path {path}'

    click.secho(to_echo)
