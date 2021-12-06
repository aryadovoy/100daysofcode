import requests
import smtplib
import datetime as dt
import time
from secret import api_key, my_email, my_pass


def send_email():
    connection = smtplib.SMTP_SSL('smtp.yandex.ru', port=465)
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg='Subject:Look up!\n\nISS is here.')
    connection.close


iss = requests.get('http://api.open-notify.org/iss-now.json').json()
iss_lat = float(iss['iss_position']['latitude'])
iss_lng = float(iss['iss_position']['longitude'])

## Get the position ##

city = 'Batumi'
# city = input('Type your city:\n')

params = {
    'q': city,
    'appid': api_key
}

location = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=params).json()
lat = location[0]['lat']
lng = location[0]['lon']

## Get sunrise and sunset ##

params = {
    'lat': lat,
    'lng': lng,
    'formatted': 0
}

sun = requests.get('https://api.sunrise-sunset.org/json', params=params).json()
sunrise = int(sun['results']['sunrise'][11:13])
sunset = int(sun['results']['sunset'][11:13])

## Check the position and time to send email ##

now = dt.datetime.utcnow().hour

while True:
    time.sleep(60)
    if now <= sunrise and now >= sunset:
        if (lat - 5) <= iss_lat <= (lat + 5) and \
        (lng - 5) <= iss_lng <= (lng + 5):
            send_email()
