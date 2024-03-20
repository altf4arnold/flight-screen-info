# flight-screen-info
Will end up being a little flask site that provides the departure schedule of whatever airport you choose (like they do in real airports)

## API : 
This program uses the API of Flightaware.
Said API requires an API key. More info [here](https://www.flightaware.com/commercial/aeroapi)

## config.py :
The example file needs to be copied as config.py. There, you can configure the API key and airport that interests you.

## datapull.py :
This file will pull the data from flightaware's server and print it on the terminal

## Flask :
This is where the web app runs. 

To start flask, ``flask run``
You can then go on ``https://127.0.0.1:5000``

# Developers : 
For the CSS, tailwind is used. 
To install the CSS bundler :
```
npm install -D tailwindcss
```
to update CSS files :
```
npx tailwindcss -i ./static/input.css -o ./static/style.css
```