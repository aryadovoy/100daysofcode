import requests
import sys
import os

sys.path.append(os.getcwd()) # for secret

import secret as s

class FlightData:
    
    def get_info(city):

        url = 'https://tequila-api.kiwi.com/locations/query'

        header = {
            'apikey': s.kiwi_key,
        }

        params = {
            'term': city,
            'location_types': 'city'
        }

        response = requests.get(url, headers=header, params=params).json()

        return response