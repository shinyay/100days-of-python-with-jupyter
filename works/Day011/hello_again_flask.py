from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return ('Hello, Flask!')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()