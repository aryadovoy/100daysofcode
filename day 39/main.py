from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt
# import json

## Checking IATA Code in sheet ##

data = DataManager.get_data_from_sheet()

for i in data:
    if i['iataCode'] == '': # TODO keyerror if 'lowestPrice' is empty
        city_data = FlightData.get_info(i['city'])
        iata = city_data['locations'][0]['code']
        DataManager.put_iata_in_sheet(i['id'], iata)

## Searching flights and sending sms ##

data = DataManager.get_data_from_sheet()

today = dt.datetime.now()
date_from = today.strftime('%d/%m/%Y')
date_to = (today + dt.timedelta(days=180)).strftime('%d/%m/%Y')

# json_data = json.dumps(FlightSearch.search_flights(i['iataCode'], date_from, date_to))

# with open('data.json', 'w') as file:
#     file.write(json_data)

for i in data:
    flight_data = FlightSearch.search_flights(i['iataCode'], date_from, date_to)
    if flight_data['data'][0]['price'] < int(i['lowestPrice']):
        text = f"{i['iataCode']}: £{flight_data['data'][0]['price']}, date: {flight_data['data'][0]['local_departure'][:10]}"
        NotificationManager.send_sms(text)
