import sqlite3
from flask import Flask
from flask import g

app = Flask(__name__)

def get_db():
    db = getattr(g,'_database', None)
    if db is None:
        db = g._database = sqlite3.connect('test_sqlite.db')
    return db

@app.teardown_appcontext
def close_connectopn(exception)