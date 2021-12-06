
import requests


url = 'https://opentdb.com/api.php'
params = {
    'amount': 10,
    'type': 'boolean'
}

question_data = requests.get(url, params=params).json()['results']
