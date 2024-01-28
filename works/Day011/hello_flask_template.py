from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_name = 'John Doe'
    return 'Hello, Flask'


@app.route('/hello')
def hello():
    user_name = 'John Doe'
    return render_template('index.html', username=user_name)

@app.route('/hello')
@app.route('/hello/<user_name>')
def hello2(user_name=None):
    return render_template('index.html', username=user_name)

if __name__ == '__main__':
    app.run()