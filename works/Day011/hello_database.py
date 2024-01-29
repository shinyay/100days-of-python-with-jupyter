import sqlite3
from flask import Flask
from flask import g
from flask import request

app = Flask(__name__)

def get_db():
    db = getattr(g,'_database', None)
    if db is None:
        db = g._database = sqlite3.connect('test_sqlite.db')
    return db

@app.teardown_appcontext
def close_connectopn(exception):
    db = getattr(g, '_database', None)
    if db is None:
        db.close()

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    if request.method == 'GET':
        return name