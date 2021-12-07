import requests
import datetime as dt
import sys
import os

sys.path.append(os.getcwd()) # for secret

import secret as s

username = 'aryadovoy'
graph_id = 'r1'
today = dt.datetime.now() - dt.timedelta(days=1)

## Creating user ##

# url = 'https://pixe.la/v1/users'

# params = {
#     'token': s.pixela_token,
#     'username': username,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }

# response = requests.post(url, json=params)
# print(response.text)

## Creating graph ##

# url = f'https://pixe.la/v1/users/{username}/graphs'

header = {
    'X-USER-TOKEN': s.pixela_token,
}

# params = {
#     'id': grap_id,
#     'name': 'reading',
#     'unit': 'page',
#     'type': 'int',
#     'color': 'kuro'
# }

# response = requests.post(url, headers=header, json=params)
# print(response.text)

## Creating a pixel ##

# url = f'https://pixe.la/v1/users/{username}/graphs/{graph_id}'

# params = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '4',
# }

# response = requests.post(url, headers=header, json=params)
# print(response.text)

## Changing ##

url = f'https://pixe.la/v1/users/{username}/graphs/{graph_id}/{today.strftime("%Y%m%d")}'

# params = {
#     'quantity': '20',
# }

# response = requests.put(url, headers=header, json=params)
# print(response.text)

## Deleting ##

response = requests.delete(url, headers=header)
print(response.text)
