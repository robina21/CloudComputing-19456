from uszipcode import SearchEngine
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
