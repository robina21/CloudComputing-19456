APP FOLDER in the Repo contains the following:

   > Docker File
 
   > Client.py - This file has both the services working together. The city names gets converted to zip code and then converted to weather Information.

Screen shots for weather client file has the following:

   > Screen of the docker file output, image output, container output and the browser outputs.


These below instructions will help to Build a Docker file, an image and a container to run a python script on the web server.

Prerequisites:
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
get_weather(zipcode)
```
Implement these 2 micro services working together:

```from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests
import http.server
import cgi
from uszipcode import SearchEngine
import requests
import json

search = SearchEngine()

"""Pass the city name and this will be converted to zip code and
the zip code will be used to find the weather
http://localhost:8000/weather/pleasanton"""

def get_weather(city):
    result = search.by_city(city)
    zipcode = result[0].zipcode
    api_key = "e116e41a98926eed847b7398fde4f339"
    url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}".format(zipcode, api_key)
    response = requests.get(url)
    data = response.json()
    data_json = json.dumps(data)
    #print(data_json)
    return data_json

#get_weather("pleasanton")
class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, data_json):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(data_json),'utf-8'))
        self.wfile.write(data_json.encode())


    def do_GET(self):
        if self.path.startswith('/weather'):
            city = self.path.split('/')[-1]
            result = get_weather(city)
            self._send_response(result)
        else:
            self.send_error(404, "Not Found: %s" % self.path)

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server...')
    httpd.serve_forever()

run()
```


Build the Image:

```docker build -t request-client .```

 
[![Picture1.png](https://i.postimg.cc/BvzVdTvX/Picture1.png)](https://postimg.cc/WDM8ZJgv)

Run The Container:

```docker run -p 8000:8000 request-client```

[![P2.png](https://i.postimg.cc/kG7MbPdr/P2.png)](https://postimg.cc/5YkWhG0p)

Check the browser to display results by passing City Name:

```http://localhost:8000/weather/pleasanton```

[![P3.png](https://i.postimg.cc/dQnwxXY1/P3.png)](https://postimg.cc/grwCwgrF)
