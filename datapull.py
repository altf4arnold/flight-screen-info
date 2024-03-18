"""
Little script written by Arnold Dechamps
"""
import config
import requests

apiUrl = "https://aeroapi.flightaware.com/aeroapi/"

airport = 'EBBR'
payload = {'max_pages': 2}
auth_header = {'x-apikey':config.FLIGHTAWAREKEY}

response = requests.get(apiUrl + f"airports/{airport}/flights",
    params=payload, headers=auth_header)

if response.status_code == 200:
    print(response.json())
else:
    print("Error executing request")

