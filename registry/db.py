import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    '''creates a connection to the SQLite database'''
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    '''checks if the connection to the db is set. If the connection exists, it is closed'''
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    '''Registers functions with the application instance'''
    app.teardown_appcontext(close_db)  # teardown_appcontext is called when cleaning up after returning a response
    app.cli.add_command(init_db_command)  # adds new command that can be called with the flask command