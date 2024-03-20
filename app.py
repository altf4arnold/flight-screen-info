"""
This piece of code was written by myself. Supposed to be a frontend for a web-page that will run on a raspi in kiosk mode
"""

import datapull
from flask import Flask, render_template
from config import AIRPORT as airport
from datetime import datetime
from dateutil import tz

app = Flask(__name__)


@app.route("/")
def hello_world():
    localformat = "%H:%M"
    rawdata = datapull.grabber()
    for flight in rawdata:
        origintimezone = flight["origin"]["timezone"]
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz(origintimezone)
        utctime = datetime.strptime(flight["scheduled_off"], "%Y-%m-%dT%H:%M:%SZ")
        utctime = utctime.replace(tzinfo=from_zone)
        flight["scheduled_off"] = utctime.astimezone(to_zone).strftime(localformat)

    return render_template('screen.html', airport=airport, data=rawdata)


@app.route("/style.css")
def style():
    with open("static/style.css", "r") as f:
        return f.read(), 200, {'Content-Type': 'text/css; charset=utf-8'}
