from flask import Flask
from flask import render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
