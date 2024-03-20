"""
This piece of code was written by myself. Supposed to be a frontend for a web-page that will run on a raspi in kiosk mode
"""

import datapull
from flask import Flask, render_template
from config import AIRPORT as airport

app = Flask(__name__)
@app.route("/")
def hello_world():
    rawdata = datapull.grabber()
    return render_template('screen.html', airport=airport, data=rawdata)


@app.route("/style.css")
def style():
    with open("static/style.css", "r") as f:
        return f.read(), 200, {'Content-Type': 'text/css; charset=utf-8'}