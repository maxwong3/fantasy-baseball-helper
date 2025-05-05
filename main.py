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

url = 'https://baseballsavant.mlb.com/leaderboard/custom?year=2025&type=batter&filter=&min=10&selections=pa%2Ck_percent%2Cbb_percent%2Cwoba%2Cxwoba%2Csweet_spot_percent%2Cbarrel_batted_rate%2Chard_hit_percent%2Cavg_best_speed%2Cavg_hyper_speed%2Cwhiff_percent%2Cswing_percent&chart=false&x=pa&y=pa&r=no&chartType=beeswarm&sort=xwoba&sortDir=desc'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = pd.read_html(url)

print(table)