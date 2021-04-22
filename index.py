from flask import Flask
from flask import request

import os
import arrow
import requests

app = Flask(__name__)
API_KEY = os.getenv('API_KEY')


@app.route('/moonphase', methods=['GET'])
def moon_phase_by_lat_lng():
    start_time = arrow.now().floor('day')
    end_time = arrow.now().shift(days=1).floor('day')

    response = requests.get(
        'https://api.stormglass.io/v2/astronomy/point',
        params={
            'lat': request.args.get('lat'),
            'lng': request.args.get('lng'),
            'start': start_time.to('UTC').timestamp(),
            'end': end_time.to('UTC').timestamp(),
        },
        headers={
            'Authorization': API_KEY
        }
    )

    return response.json()


@app.route('/weather', methods=['GET'])
def weather_info_by_lat_lng():
    start_time = arrow.now().floor('day')
    end_time = arrow.now().ceil('day')

    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': request.args.get('lat'),
            'lng': request.args.get('lng'),
            'params': ','.join(['airTemperature', 'humidity']),
            'start': start_time.to('UTC').timestamp(),
            'end': end_time.to('UTC').timestamp(),
        },
        headers={
            'Authorization': API_KEY
        }
    )

    return response.json()
