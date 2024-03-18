"""
Little script written by Arnold Dechamps
"""
import config
import requests

apiUrl = "https://aeroapi.flightaware.com/aeroapi/"

airport = config.AIRPORT
payload = {'max_pages': 2}
auth_header = {'x-apikey':config.FLIGHTAWAREKEY}

response = requests.get(apiUrl + f"airports/{airport}/flights/scheduled_departures",
    params=payload, headers=auth_header)

if response.status_code == 200:
    departures = response.json()
    print(departures)
else:
    print("Error executing request")

