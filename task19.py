# Области
import requests
import json

API_KEY = '48816329-7532-4737-8718-e8cd550efe71'
URL1 = 'https://geocode-maps.yandex.ru/1.x/?apikey=%s&format=json&geocode=%s'


address = input()
page = requests.get(URL1 % (API_KEY, address))
d = json.loads(page.text)
GeoObjectCollection = d['response']['GeoObjectCollection']
GeoObject = GeoObjectCollection['featureMember'][0]['GeoObject']
Point = GeoObject['Point']['pos']
print(Point)

URL2 = 'https://geocode-maps.yandex.ru/1.x\
        /?apikey=%s&format=json&geocode=%s&kind=metro&results=1'

page = requests.get(URL2 % (API_KEY, Point.replace(" ", ",")))
d = json.loads(page.text)
GeoObjectCollection = d['response']['GeoObjectCollection']
GeoObject = GeoObjectCollection['featureMember'][0]['GeoObject']
result = GeoObject['metaDataProperty']['GeocoderMetaData']['text']
print(result)
