# Южный город
import requests
import json

API_KEY = '48816329-7532-4737-8718-e8cd550efe71'
URL = 'https://geocode-maps.yandex.ru/1.x/?apikey=%s&format=json&geocode=%s'


str_input = input()
cities = str_input.split(",")
min_south = 1000
min_city = ""

for city in cities:
    page = requests.get(URL % (API_KEY, city.strip()))
    d = json.loads(page.text)
    GeoObjectCollection = d['response']['GeoObjectCollection']
    GeoObject = GeoObjectCollection['featureMember'][0]['GeoObject']
    Point = GeoObject['Point']['pos']
    south = Point.split()[1]
    if float(south) < min_south:
        min_south = float(south)
        min_city = city

print(min_city)
