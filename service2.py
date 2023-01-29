import requests
import json
import sys

"""Displays weather information when zip code is passed"""

def get_weather(zipcode):
    api_key = "e116e41a98926eed847b7398fde4f339"
    url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}".format(zipcode, api_key)
    response = requests.get(url)
    weather_data = json.loads(response.text)
    print(f"The weather data for {zipcode} is --->", weather_data)
    return weather_data

zipcode = sys.argv[1]
get_weather(zipcode)
