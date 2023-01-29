Read me for Build a Dockerfile, Image, and Container



APP FOLDER contains the following:

Make these two microservices work together (Optional).
 
the client.py file has the both the services working together.
The city names gets converted to zip code and then converted to weather.

From the browser pass the city name and it will output the weather on the UI


Screen shots for weather client file has the following:

Screen of the docker file output, image output, container output and the browser outputs.

Build a Dockerfile, Image, and Container
Getting Started
These instructions will help to Build a Docker file, an image and a container to run a python script on the web server
Prerequisites
•	Docker
•	Libraries: Requests, uszipcode 

Build Service 1:

```from uszipcode import SearchEngine
import sys
"""Takes City name as variable and prints ZIP CODE"""
search = SearchEngine()

def get_zipcode(city_name):
    result = search.by_city(city_name)
    if result:
        print(f"The Zip Code for {city_name} is --> ", result[0].zipcode)
        return result[0].zipcode

    else:
        return None

city_name = sys.argv[1]
get_zipcode(city_name)
```

Build Service 2:

```import requests
import json
import sys
"""Takes Zip code as variable and outputs weather"""

def get_weather(zipcode):
    api_key = "e116e41a98926eed847b7398fde4f339"
    url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}".format(zipcode, api_key)
    response = requests.get(url)
    weather_data = json.loads(response.text)
    print(f"The weather data for {zipcode} is --->", weather_data)
    return weather_data

zipcode = sys.argv[1]
get_weather(zipcode)```

Build the Image:

```docker build -t request-client .```

 
[![Picture1.png](https://i.postimg.cc/BvzVdTvX/Picture1.png)](https://postimg.cc/WDM8ZJgv)

Run The Container:

```docker run -p 8000:8000 request-client```

[![P2.png](https://i.postimg.cc/kG7MbPdr/P2.png)](https://postimg.cc/5YkWhG0p)

Check the browser to display results by passing City Name:

```http://localhost:8000/weather/pleasanton```

[![P3.png](https://i.postimg.cc/dQnwxXY1/P3.png)](https://postimg.cc/grwCwgrF)
