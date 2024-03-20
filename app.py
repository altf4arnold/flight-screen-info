"""
This piece of code was written by myself. Supposed to be a frontend for a web-page that will run on a raspi in kiosk mode
"""

import datapull
from flask import Flask, render_template
from datetime import datetime, timedelta
from dateutil import tz

app = Flask(__name__)


@app.route("/")
def hello_world():
    localformat = "%H:%M"
    rawdata = datapull.grabber()
    airport={"name":"","icao":"", "iata":""}
    for flight in rawdata:
        # Source Airport naming
        airport["name"] = flight["origin"]["name"]
        airport["icao"] = flight["origin"]["code_icao"]
        airport["iata"] = flight["origin"]["code_iata"]

        # Converting departures time from UTC to local time
        origintimezone = flight["origin"]["timezone"]
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz(origintimezone)
        utctime = datetime.strptime(flight["scheduled_off"], "%Y-%m-%dT%H:%M:%SZ")
        utctime = utctime.replace(tzinfo=from_zone)
        flight["scheduled_off"] = utctime.astimezone(to_zone).strftime(localformat)

        # Calculating Delays in human readable ways
        negative = False
        delay = flight["departure_delay"]
        if delay != 0:
            if delay is not None:
                # taking advances in account
                if delay < 0:
                    # delay is negative
                    negative = True
                    delay = abs(delay)
                delay = timedelta(seconds=delay)
                delay = datetime.strptime(str(delay), "%H:%M:%S")
                flight["departure_delay"] = delay.strftime(localformat)
                if negative:
                    flight["departure_delay"] = ("-" + str(flight["departure_delay"]))
    return render_template('screen.html', airport=airport, data=rawdata)


@app.route("/style.css")
def style():
    with open("static/style.css", "r") as f:
        return f.read(), 200, {'Content-Type': 'text/css; charset=utf-8'}
