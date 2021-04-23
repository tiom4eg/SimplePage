from flask import Flask

app = Flask(__name__)


@app.route('/')
def landing():
    return "Hello, Github Pages!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
