from http.server import BaseHTTPRequestHandler, HTTPServer
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
