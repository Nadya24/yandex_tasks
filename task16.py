import pygame, requests, sys, os

# Создайте оконное приложение, отображающее карту по координатам и в масштабе, который задаётся программно.

# class MapParams(object):
#     def __init__(self):
#         self.lat =  25.694768  # Координаты центра карты на старте. Задал координаты университета
#         self.lon = 133.795384
#         self.zoom = 4  # Масштаб карты на старте. Изменяется от 1 до 19
#         self.type = "sat" # Другие значения "sat", "sat,skl"
#     # Преобразование коорднат в параметр ll, требуется без пробелов, через запятую и без скобок
#     def ll(self):
#         return '%s%s'%(str(self.lon), '%2C')+"-"+str(self.lat)

# Создание карты с соответствующими параметрами.
#

def load_map():
    lines = "29.915992,59.891371,29.942943,59.896029,30.166776,59.919017,30.262215,59.917334,30.268722,59.922877,30.280356,59.933270,30.312075,59.941932&z=10"
    map_request = "https://static-maps.yandex.ru/1.x/?lang=ru_RU&l=map&pl=%s" % lines
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
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:  # Выход из программы
           break
        #Создаем файл
        map_file = load_map()
        # Рисуем картинку, загружаемую из только что созданного файла.
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    # Удаляем файл с изображением.
    os.remove(map_file)

if __name__ == "__main__":
    main()
