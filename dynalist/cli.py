import logging
import click
import keyring 
from dynalist import Dynalist
from tabulate import tabulate
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import Condition
from .exceptions import InvalidTokenError, RateLimitedError
from .helpers import token_exists, set_token, reset_token, get_token, PERMISSIONS

TABLE_FMT = "psql"

@click.group()
@click.pass_context
def cli(ctx):
    logger = logging.getLogger('dynalist')
    ctx.obj["LOGGER"] = logger

    if token_exists():    
        dyn = Dynalist(get_token())
        ctx.obj["CLIENT"] = dyn
    else:
        ctx.invoke(token)

@cli.command()
@click.argument('token', required=False)
@click.option('--reset/--no-reset', default=False)
@click.option('--delete/--no-delete', default=False)
@click.pass_context
def token(ctx, token, reset, delete):
    if token:
        set_token(token)
    else:
        if not token_exists():
            hidden = [True]  # Nonlocal
            bindings = KeyBindings()

            @bindings.add('c-t')
            def _(event):
                ' When ControlT has been pressed, toggle visibility. '
                hidden[0] = not hidden[0]

            print('Type Control-T to toggle password visible.')
            token = prompt('Password: ',
                            is_password=Condition(lambda: hidden[0]),
                            key_bindings=bindings)

            set_token(token)
            click.echo("Token Set")
        else:
            if reset:
                reset_token()
                new_token = prompt('Enter your new Token: ', is_password=True)
                set_token(new_token)
            if delete:
                reset_token()
            else:
                click.echo("Token already set - ready to go!")


@cli.command()
@click.pass_context
def docs(ctx):
    logger = ctx.obj["LOGGER"]
    dyn = ctx.obj["CLIENT"]

    try:
        res = dyn.all()
        docs = [[doc["id"], doc["title"], PERMISSIONS[doc["permission"]]] for doc in res["files"] if doc["type"] == "document"]
        print(tabulate(docs, headers=["ID", "TITLE", "PERMISSION"], tablefmt=TABLE_FMT))

    except (InvalidTokenError, RateLimitedError) as e:
        logger.error(e.message)


@cli.command()
@click.pass_context
def folders(ctx):
    logger = ctx.obj["LOGGER"]
    dyn = ctx.obj["CLIENT"]

    try:
        res = dyn.all()
        docs = [[doc["id"], doc["title"], PERMISSIONS[doc["permission"]]] for doc in res["files"] if doc["type"] == "folder"]
        print(tabulate(docs, headers=["ID", "TITLE", "PERMISSION"], tablefmt=TABLE_FMT))

    except (InvalidTokenError, RateLimitedError) as e:
        logger.error(e.message)


@cli.command()
@click.argument('message')
@click.option('--note', help='Optional note to add')
@click.pass_context
def inbox(ctx, message, note):
    logger = ctx.obj["LOGGER"]
    dyn = ctx.obj["CLIENT"]

    dyn.to_inbox(message, note)


def main():
    cli(obj={})

if __name__ == "__main__":
    main()