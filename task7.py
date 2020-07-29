# Парсинг словаря
# Иногда в качестве параметров в командной строке передаются данные вида
#  "ключ=значение причем количество таких параметров заранее неизвестно.
# Напишите программу, которая разбирает такие параметры
# и выводит их на экран в виде:
# "Key: ключ Value: значение

# при этом каждая пара выводится на отдельной строке.
# Еще программа должна принимать опцию —sort,
# которая позволяет упорядочивать выводимые значения по ключу.

# И конечно же, вам необходимо использовать библиотеку argparse.
# Пример 1
# Ввод Вывод
# python3 solution.py —sort name=Vasya surname=Ivanov age=25
# Key: age Value: 25
# Key: name Value: Vasya
# Key: surname Value: Ivanov
# Пример 2
# Ввод Вывод
# python3 solution.py name=Vasya surname=Ivanov age=25
# Key: name Value: Vasya
# Key: surname Value: Ivanov
# Key: age Value: 25
# Примечания
# Проверка валидности входных параметров не требуется.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sort', action="store_true")
parser.add_argument('just_params', nargs='*',
                    type=str)

args = parser.parse_args()

if args.sort:
    res_list = {key_value.split("=")[0]:
                key_value.split("=")[1] for key_value in args.just_params}
    for key in sorted(res_list.keys()):
        spaceplus = 13 - len(key)
        print("Key: %s%s" % (key, " " * spaceplus),
              "Value: %s" % res_list[key])

elif args.just_params:
    res_list = {key_value.split("=")[0]: key_value.split("=")[1]
                for key_value in args.just_params}
    for key in res_list.keys():
        spaceplus = 13 - len(key)
        print("Key: %s%s" % (key, " " * spaceplus),
              "Value: %s" % res_list[key])
