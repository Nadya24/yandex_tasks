# Округа
import requests
import json

API_KEY = '48816329-7532-4737-8718-e8cd550efe71'
CITIES = ['г.Хабаровск', 'г.Уфа', 'г.Нижний Новгород', 'г.Калининград']
URL = 'https://geocode-maps.yandex.ru/1.x/?apikey=%s&format=json&geocode=%s'

for city in CITIES:
    page = requests.get(URL % (API_KEY, city))
    d = json.loads(page.text)
    GeoObjectCollection = d['response']['GeoObjectCollection']
    GeoObject = GeoObjectCollection['featureMember'][0]['GeoObject']
    Address = GeoObject['metaDataProperty']['GeocoderMetaData']['Address']
    print(Address['Components'][1]['name'])
