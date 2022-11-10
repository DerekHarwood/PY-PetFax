from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is a Flask app"

@app.route('/pets')
def pets():
    return "These are our pets available for adoption!"

