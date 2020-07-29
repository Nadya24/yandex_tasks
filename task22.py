# Останкинская телебашня вещает в эфир радиоволны дециметрового диапазона.

# Дальность приёма в условиях прямой видимости вычисляется по формуле:
# l = 3,6(√h1 + √h2 ) (км), где h1 и h2 —
# высоты расположения передающей и приёмной антенн (м).

# Считая, что высота телебашни
# (передающей антенны) равна 525 метров, определить,
# на какую высоту должна быть поднята приёмная антенна в заданной точке.

# Ваша программа

# представляет собой консольное приложение,
# анализируемый населённый пункт или адрес вводится с клавиатуры.

# Программа должна напечатать минимальную высоту приёмной антенны (в метрах),
# обеспечивающей приём сигнала непосредственно с телебашни.
#
# ---------------------
# -
# -

# 1Найти расстояние между Останкинской башней и адресом
# Найти высоту башни


from geopy.distance import geodesic
import requests
import json

API_KEY = '48816329-7532-4737-8718-e8cd550efe71'
URL = 'https://geocode-maps.yandex.ru/1.x/?apikey=%s&format=json&geocode=%s'


def main():
    from_addr = "Москва, Останкинская башня"
    to_addr = input("Укажите адрес телебашни")
    dist = 0
    lat = []
    lon = []

    for address in [from_addr, to_addr]:
        page = requests.get(URL % (API_KEY, address.strip()))
        d = json.loads(page.text)
        GeoObjectCollection = d['response']['GeoObjectCollection']
        GeoObject = GeoObjectCollection['featureMember'][0]['GeoObject']
        # print(GeoObject)
        Point = GeoObject['Point']['pos']
        # print(Point)
        lat.append(Point.split(" ")[0])
        # print(lat)
        lon.append(Point.split(" ")[1])
        # print(lon)
    dist += geodesic((float(lat[0]), float(lon[0])),
                     (float(lat[1]), float(lon[1]))).km

    print(dist)
    l = dist
    h2 = pow((l/3.6 - pow(525, 0.5)), 2)
    print("Высота телебашни в метрах", h2)
    # l = 3,6(√h1 + √h2 ) (км), где h1 и h2 —
    # высоты расположения передающей и приёмной антенн (м).\


if __name__ == "__main__":
    main()
