from os import times
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt
# import json

## Checking IATA Code in sheet ##

data = DataManager.get_data_from_prices()

for i in data:
    if i['iataCode'] == '': # TODO keyerror if 'lowestPrice' is empty
        city_data = FlightData.get_info(i['city'])
        iata = city_data['locations'][0]['code']
        DataManager.put_iata_in_sheet(i['id'], iata)

## Searching flights and sending sms ##

data = DataManager.get_data_from_prices()

today = dt.datetime.now()
date_from = today.strftime('%d/%m/%Y')
date_to = (today + dt.timedelta(days=180)).strftime('%d/%m/%Y')

# json_data = json.dumps(FlightSearch.search_flights('DPS', date_from, date_to, stops=2))

# with open('data.json', 'w') as file:
#     file.write(json_data)

users_data = DataManager.get_data_from_users()

for i in data:
    flight_data = FlightSearch.search_flights(i['iataCode'], \
        date_from, date_to)
    try:
        flight_data['data'][0]['price']
        text = (
                f"{i['iataCode']}: £{flight_data['data'][0]['price']}, " \
                f"date: {flight_data['data'][0]['local_departure'][:10]}"
            )
    except IndexError:
        flight_data = FlightSearch.search_flights(i['iataCode'], \
            date_from, date_to, stops=2)
        text = (
                f"{i['iataCode']} via " \
                f"{flight_data['data'][0]['route'][0]['cityCodeTo']}: " \
                f"£{flight_data['data'][0]['price']}, date: " \
                f"{flight_data['data'][0]['local_departure'][:10]}"
            )
    if flight_data['data'][0]['price'] < int(i['lowestPrice']):
        for i in users_data:
            fly_to = str(flight_data['data'][0]['local_departure'])[:10]
            return_fly = str((dt.datetime.strptime(fly_to, '%Y-%m-%d') + \
                dt.timedelta(days=flight_data['data'][0]['nightsInDest'])))[:10]

            NotificationManager.send_email(i['firstName'], i['email'],
                flight_data['data'][0]['routes'][0][0],
                flight_data['data'][0]['routes'][0][1],
                flight_data['data'][0]['routes'][1][0],
                flight_data['data'][0]['routes'][1][1],
                fly_to, return_fly,
                text.replace('£', '£'.encode('ascii', 'ignore').decode('ascii')))
