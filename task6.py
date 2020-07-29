# Мега cat
# Напишите программу, которая в качестве аргумента принимает имя файла
# (не указан файл или указан несуществующий — ошибка)
#  и выводит его содержимое на экран.
# В добавок, программа может принимать дополнительные агрументы:
# «--count» для вывода кол-ва строк в конце сообщения,
# «--num» для вывода порядкового номера с пробелом в начале каждой строки,
# «--sort» для сортировки строк в алфавитном порядке перед выводом.
# Пусть файл text1.txt содержит строки:

# Houston
# we have
# a problem

# Пример 1
# Ввод Вывод
# python3 solution.py —num text1.txt
# 0 Houston
# 1 we have
# 2 a problem
# Пример 2
# Ввод Вывод
# python3 solution.py —count —sort text1.txt
# Houston
# a problem
# we have
# rows count: 3
# Пример 3
# Ввод Вывод
# python3 solution.py —count —sort textX.txt
# ERROR
# Примечания
# Необходимо использовать библиотеку argparse
# ------------------------------------------------------------------------------------------------------------------------------------------

import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('--count', action="store_true")
parser.add_argument('--num', action="store_true")
parser.add_argument('--sort', action="store_true")
parser.add_argument('filename', nargs='?')

args = parser.parse_args()


if not args.filename:
    print("ERROR")
else:
    input_file = args.filename
    if os.path.exists(input_file):

        count = args.count
        num = args.num
        sort_lines = args.sort
        res = ''
        with open(input_file, 'r') as f:
            res = f.readlines()

        if sort_lines:
            res.sort()

        if num:
            res = ["%s %s" % (inx, val) for inx, val in enumerate(res)]

        if count:
            res.append("rows count: %s" % len(res))

        for r in res:
            print(r.replace("\n", ""))
    else:
        print("ERROR")
