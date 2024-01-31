from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask import g
import sqlite3

app = Flask(__name__)

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