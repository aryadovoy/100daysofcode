from twilio.rest import Client
import requests
import sys
import os

sys.path.append(os.getcwd()) # for secret

import secret as s

params = {
    'q': 'Moscow',
    'appid': s.owm_api_key
}

location = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=params).json()
lat = location[0]['lat']
lng = location[0]['lon']

url = 'https://api.openweathermap.org/data/2.5/onecall'

params = {
    'lat': lat,
    'lon': lng,
    'appid': s.owm_api_key,
    'exclude': 'current,minutely,daily',
}

response = requests.get(url, params=params).json()

for i in range(12):
    if response['hourly'][i]['weather'][0]['id'] < 700:
        client = Client(s.twilio_account_sid, s.twilio_auth_token)

        message = client.messages \
                        .create(
                            body=f"It will be rainy in next {i} hours.",
                            from_='+13862844975',
                            to=s.my_num,
                        )
        print(message.status)
        break
