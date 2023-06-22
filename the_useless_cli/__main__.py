# The Useless CLI
# GNU GPLv3
# Copyright (C) 2023 ItsQuadrus
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it under certain conditions.
# See the LICENSE file for details.

import typer
import random
import string
import shutil
import requests
from the_useless_cli.constants import VERSION

app = typer.Typer()
terminal_width, _ = shutil.get_terminal_size()
sep = '─' * terminal_width


@app.command()
def about():
    """Shows information about the CLI and its author."""
    typer.echo(sep)
    typer.echo(f'The Useless CLI - Version {VERSION}')
    typer.echo("Copyright (C) 2023 ItsQuadrus")
    typer.echo('''
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
''')
    typer.echo(sep)

@app.command()
def number(num: int = 100):
    """Prints a random number between 0 and the specified number."""
    typer.echo(random.randint(0, num))

@app.command()
def number2(num1: int, num2: int):
    """Prints a random number between the two specified numbers."""
    typer.echo(random.randint(num1, num2))

@app.command()
def word(length: int = 0):
    """Prints a random word from a US dictionary."""
    if length == 0:
        # Get a random word
        r = requests.get("https://random-word-api.herokuapp.com/word")
        typer.echo(r.json()[0])
    else:
        try: # get word of specific length
            r = requests.get(f"https://random-word-api.herokuapp.com/word?length={length}")
            typer.echo(r.json()[0])
        except IndexError as e:
            typer.echo(f'No words found with length {length}', err=True)

@app.command()
def color(type: str = 'hex'):
    """Prints a random color in the specified format. Valid formats are: hex, rgb, hsl, hsv, cmyk. Default is hex."""
    if type == 'hex':
        typer.echo('#' + ''.join(random.choices(string.hexdigits, k=6)))
    elif type == 'rgb':
        typer.echo(f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})')
    elif type == 'hsl':
        typer.echo(f'hsl({random.randint(0, 360)}, {random.randint(0, 100)}%, {random.randint(0, 100)}%)')
    elif type == 'hsv':
        typer.echo(f'hsv({random.randint(0, 360)}, {random.randint(0, 100)}%, {random.randint(0, 100)}%)')
    elif type == 'cmyk':
        typer.echo(f'cmyk({random.randint(0, 100)}%, {random.randint(0, 100)}%, {random.randint(0, 100)}%, {random.randint(0, 100)}%)')
    else:
        typer.echo(f'Invalid color type: {type}')

@app.command()
def password(length: int = 16):
    """Prints a random password with the specified length."""
    if length > 32:
        typer.echo('Password length cannot be greater than 32')
    else:
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(alphabet, k=length))
        typer.echo(password)

if __name__ == '__main__':
    app() 