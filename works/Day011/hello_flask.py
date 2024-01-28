from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask'

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()