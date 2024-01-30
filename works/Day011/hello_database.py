import sqlite3
from flask import Flask
from flask import g
from flask import request

app = Flask(__name__)

### Connect Database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('hello_sqlite.db')
    return db

### Close Database
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def employee():
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

    if request.method == 'POST':
        curs.execute(f'INSERT INTO persons(name) values("{name}")')
        db.commit()
        return f'created {name}', 201

    if request.method == 'PUT':
        new_name = request.values['new_name']
        curs.execute(f'UPDATE persons set name = "{new_name}" '
                     f'WHERE name = "{name}"')
        db.commit()
        return f'updated {name}: {new_name}', 200

    if request.method == 'DELETE':
        curs.execute(f'DELETE from persons WHERE name = "{name}"')
        db.commit()
        return f'deleted {name}', 200

    curs.close()



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