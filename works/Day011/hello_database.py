import sqlite3
from flask import Flask
from flask import g
from flask import request

app = Flask(__name__)

def get_db():
    db = get_db()
    curs = db.cursor()
    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons( '
        'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    db.commit()

    name = request.values.get('name', name)

    if request.method == 'GET':
        curs.execute(f'SELECT * FROM persons WHERE name = "{name}"')
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        return f'{user_id}:{name}', 200


    curs.close()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    db.commit()

    if request.method == 'GET':
        return name

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()