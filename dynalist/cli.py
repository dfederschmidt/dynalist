import click
from dynalist import Dynalist
import pprint
from tabulate import tabulate
import keyring 
from helpers import token_exists, set_token, reset_token, get_token
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import Condition

TABLE_FMT = "psql"

@click.group()
@click.pass_context
def cli(ctx):
    if token_exists():    
        dyn = Dynalist(get_token())
        ctx.obj["CLIENT"] = dyn
    else:
        ctx.invoke(token)

@cli.command()
@click.option('--reset/--no-reset', default=False)
@click.option('--delete/--no-delete', default=False)
@click.pass_context
def token(ctx, reset, delete):
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
            set_token(token)
        if delete:
            reset_token()
        else:
            click.echo("Token already set - ready to go!")

@cli.command()
@click.option("--id")
@click.pass_context
def docs(ctx, id):
    dyn = ctx.obj["CLIENT"]
    if id:
        res = dyn.doc(id)
        print(res)
    else:
        res = dyn.all()
        docs = [[doc["id"], doc["title"]] for doc in res["files"] if doc["type"] == "document"]
        print(tabulate(docs, headers=["ID", "TITLE"], tablefmt=TABLE_FMT))

@cli.command()
@click.pass_context
def folders(ctx):
    dyn = ctx.obj["CLIENT"]
    res = dyn.all()
    docs = [[doc["id"], doc["title"]] for doc in res["files"] if doc["type"] == "folder"]
    print(tabulate(docs, headers=["ID", "TITLE"], tablefmt=TABLE_FMT))


if __name__ == "__main__":
    cli(obj={})