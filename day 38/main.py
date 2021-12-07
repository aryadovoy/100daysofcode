import requests
import datetime as dt
import sys
import os

sys.path.append(os.getcwd()) # for secret

import secret as s


def push_to_sheet(activity, duration, calories):
    url = 'https://api.sheety.co/65fa3abfcd1ea253c7307ccff20de618/myWorkouts/workouts'

    header = {
        'Authorization': s.sheety_key,
        'Content-Type': 'application/json'
    }

    params = {
        'workout': {
            'date': dt.datetime.now().strftime('%d/%m/%Y'),
            'time': dt.datetime.now().strftime('%X'),
            'exercise': activity.title(),
            'duration': duration,
            'calories': calories
        }
    }

    response = requests.post(url, headers=header, json=params)
    print(response.text)


query = input('Type your text: ') # Ran 3 km

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

header = {
    'x-app-id': s.nutritionix_id,
    'x-app-key': s.nutritionix_key,
    'Content-Type': 'application/json',
}

params = {
    'query': query,
}

response = requests.post(url, headers=header, json=params)
for i in response.json()['exercises']:
    push_to_sheet(i['name'], i['duration_min'], i['nf_calories'])
