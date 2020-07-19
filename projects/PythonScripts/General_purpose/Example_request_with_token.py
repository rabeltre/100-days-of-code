import requests

url = 'https://api.github.com/user'



#get the data about the photos
response = requests.get(url, headers={'Authorization': 'Bearer 5f3ab8db99613218c350b5177efd92849db70644 '})

for item in response.json():
    print(f'{item}: {response.json()[item]}')
