
import urllib.parse

import requests


api_address = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = 'yhz'

url = api_address + urllib.parse.urlencode({'address':address}) 
json_data = requests.get(url).json() 
print(json_data)
