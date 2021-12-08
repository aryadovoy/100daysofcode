import requests


class DataManager:

    def get_data_from_sheet():
        
        url = 'https://api.sheety.co/65fa3abfcd1ea253c7307ccff20de618/flightDeals/prices'

        response = requests.get(url).json()['prices']
        return response

    
    def put_iata_in_sheet(id, iata):
        
        url = f'https://api.sheety.co/65fa3abfcd1ea253c7307ccff20de618/flightDeals/prices/{id}'

        params = {
            'price': {
                'iataCode': iata,
            }
        }

        response = requests.put(url, json=params).json()
        print(response)
