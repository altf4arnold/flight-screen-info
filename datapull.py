"""
Little script written by Arnold Dechamps
"""
import config
import requests


def grabber():
    """
    Main function to pull data from flightaware API. Mostly flightaware code with overhead. Will modify if needed
    :return: raw data
    """
    departures = []
    apiUrl = "https://aeroapi.flightaware.com/aeroapi/"
    airport = config.AIRPORT
    payload = {'max_pages': config.PAGES}
    auth_header = {'x-apikey': config.FLIGHTAWAREKEY}

    response = requests.get(apiUrl + f"airports/{airport}/flights/scheduled_departures", params=payload,
                            headers=auth_header)
    if response.status_code == 200:
        departures = response.json()["scheduled_departures"]
    else:
        print("Error executing request")

    # These are for debug. Should be commented in production
    """
    for flight in departures:
        print(flight)
    """
    return departures


if __name__ == '__main__':
    departures = grabber()
    name = "unknown"
    operator = "unknown"
    scheduled_off = "unknown"
    destination = "unknown"
    acfttype = "unknown"
    print("Flight  Operator   Time    Destination              acft-type")
    for flight in departures:
        if flight["ident"] is not None:
            name = flight["ident"]
        if flight["operator"] is not None:
            operator = flight["operator"]
        if flight["scheduled_off"] is not None:
            scheduled_off = flight["scheduled_off"]
        if flight["destination"] is not None:
            if flight["destination"]["name"] is not None:
                destination = (flight["destination"]["code_icao"] + " " + flight["destination"]["name"])
        if flight["aircraft_type"] is not None:
            acfttype = flight["aircraft_type"]

        print(name + "  " + operator + " " + scheduled_off + " " + destination + " " + acfttype)
