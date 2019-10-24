from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/about")
def about():
    return "Let's return an actual page that describes the project"
