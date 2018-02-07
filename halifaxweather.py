import requests
api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=8346be2f812b9334069f9b96f46327f9&q='
city = input("City Name : ")

url = api_address+city
json_data = requests.get(url).json()

print(json_data)
