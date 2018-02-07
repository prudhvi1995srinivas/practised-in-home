
import urllib.parse

import requests


api_address = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('address: ')
    url = api_address + urllib.parse.urlencode({'address':address})
    print(url)
    json_data = requests.get(url).json() 
    print(json_data)

    json_status = json_data['status']
    print('API Status:' + json_status)
 
