import pygame
import requests
import sys
import os


class MapParams(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.zoom = 4
        self.type = "sat"

    def ll(self):
        return '%s%s' % (str(self.lon), '%2C') + "-" + str(self.lat)


def load_map(mp, i):
    map_request = "http://static-maps.yandex.ru/1.x/?ll\
                  ={ll}&z={z}&l={type}".format(
                  ll=mp.ll(), z=mp.zoom, type=mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запись полученного изображения в файл.
    map_file = "%s.png" % i
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file


def main():
    # Инициализируем pygame
    num = 0
    list_coordinate = [{'lat': 25.120358, 'lon': 55.130689},
                       {'lat': 8.243002, 'lon': 115.406966},
                       {'lat': 41.115700, 'lon': 29.068548}]
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    while True:
        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.KEYDOWN:
                if num == 3:
                    num = 0
                mp = MapParams(list_coordinate[num]['lat'],
                               list_coordinate[num]['lon'])
                map_file = load_map(mp, num)
                # Рисуем картинку, загружаемую из только что созданного файла.
                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.flip()
                num += 1

    pygame.quit()
    # Удаляем файл с изображением.
    os.remove(map_file)


if __name__ == "__main__":
    main()
