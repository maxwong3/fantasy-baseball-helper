from flask import Flask
from flask import render_template
from markupsafe import escape
from bs4 import BeautifulSoup
import requests
import pandas as pd


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

url = 'https://www.baseball-reference.com/leagues/majors/2025-standard-batting.shtml'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all('table')

print(table)