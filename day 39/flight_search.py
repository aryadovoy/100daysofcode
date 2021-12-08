import requests
import sys
import os

sys.path.append(os.getcwd()) # for secret

import secret as s

class FlightSearch:
    
    def search_flights(fly_to, date_from, date_to):
        
        url = 'https://tequila-api.kiwi.com/v2/search'

        header = {
            'apikey': s.kiwi_key,
        }

        params = {
            'fly_from': 'LON',
            'fly_to': f'city:{fly_to}',
            'date_from': date_from,
            'date_to': date_to,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'curr': 'GBP',
            'max_stopovers': 0,
            'sort': 'price',
            'limit': 3,
        }

        response = requests.get(url, headers=header, params=params).json()

        return response