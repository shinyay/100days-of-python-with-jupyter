from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask import g
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'hello_sqlite3.db'

# Connect Database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

# Initilize Database
def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                done BOOLEAN NOT NULL
            )
                   ''')
        db.commit

# Teardown to close the Database Connection
@app.teardown_appcontext
def close_db(exeception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Initiliaze Database before First Request
@app.before_request
def before_first_request():
    init_db()

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    db = get_db()
    cursor = db.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    cursor.close()

    task_list = [{'id': task['id'], 'title': task['title'], 'description': task['description'], 'done': task['done']} for task in tasks]
    return jsonify({'tasks': task_list})
    

@app.route('/')
def home():
    return ('Hello, Flask!')

@app.route('/hello/<name>')
def hello(name):    
    return f'Hello, {name}!'

@app.route('/hello/template/<name>')
def template(name):
    return render_template('/index.html', username=name)



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()