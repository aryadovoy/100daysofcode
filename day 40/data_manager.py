import requests


class DataManager:

    def get_data_from_prices():
        
        url = 'https://api.sheety.co/65fa3abfcd1ea253c7307ccff20de618/flightDeals/prices'

        response = requests.get(url).json()['prices']
        return response

    def get_data_from_users():
        
        url = 'https://api.sheety.co/65fa3abfcd1ea253c7307ccff20de618/flightDeals/users'

        response = requests.get(url).json()['users']
        return response    

    def put_iata_in_sheet(id, iata):
        
        url = f'https://api.sheety.co/65fa3abfcd1ea253c7307ccff20de618/flightDeals/prices/{id}'

        params = {
            'price': {
                'iataCode': iata,
            }
        }

        requests.put(url, json=params).json()

    def add_user():
        
        print('Welcome to Flight Club')
        fname = input('Your first name:\n')
        lname = input('Your last name:\n')
        email = input('Your email:\n')
        
        url = 'https://api.sheety.co/65fa3abfcd1ea253c7307ccff20de618/flightDeals/users'

        params = {
            'user': {
                'firstName': fname,
                'lastName': lname,
                'email': email,
            }
        }
        
        requests.post(url, json=params).json()
        print('Your info was added!')
