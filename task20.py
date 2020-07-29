# Длина пути
# Определите длину пути, заданного последовательностью точек.

# Отобразите заданный путь на карте, а в средней его точке поставьте метку.

# Последовательность точек задайте по своему усмотрению,
# например, списком координат.

from geopy.distance import geodesic
import pygame
import requests
import sys
import os


def load_map():
    lines = "29.915992,59.891371,29.942943,59.896029,30.166776,59.919017,30.262215,59.917334,\
    30.268722,59.922877,30.280356,59.933270,30.312075,59.941932&z=10"
    map_request = "https://static-maps.yandex.ru/1.x/?lang=ru_RU&l=map&pl=%s&pt=\
    30.262215,59.917334" % lines
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запись полученного изображения в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file


def main():
    lat = [29.915992, 29.942943, 30.166776, 30.262215,
           30.268722, 30.280356, 30.312075]
    lon = [59.891371, 59.896029, 59.919017, 59.917334,
           59.922877, 59.933270, 59.941932]

    dist = 0
    for i in range(len(lat)):
        dist += geodesic(lat[i], lon[i]).km

    print(dist)
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:  # Выход из программы
            break
        map_file = load_map()
        # Рисуем картинку, загружаемую из только что созданного файла.
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    # Удаляем файл с изображением.
    os.remove(map_file)


if __name__ == "__main__":
    main()
