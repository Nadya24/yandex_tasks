# Калькулятор 3.0
# Настала очередь третьей модификации нашего целочисленного
# калькулятора-сумматора.
# Для правильной работы он должен получить два целочисленных параметра.
# При этом параметры могут быть ошибочными.
# Вам

# необходимо посчитать сумму переданных параметров.
# Если параметры не были переданы, то следует вывести фразу NO PARAMS,
# если целочисленный параметр только один, то выведите фразу TOO FEW PARAMS,
# если же целочисленных параметров больше двух — TOO MUCH PARAMS,
# а в случае других ошибок — имя класса исключения,
# которое Python выбросит в этом случае.

# Только не думайте, что все так просто: вам необходимо обязательно
# использовать библиотеку argparse
# Пример 1
# Ввод Вывод
# python3 solution.py 3 5
# 8
# Пример 2
# Ввод Вывод
# python3 solution.py 3
# TOO FEW PARAMS
#
#
import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('chars', nargs='*')

    args = parser.parse_args()

    if (len(args.chars) == 2):
        print(int(args.chars[0]) + int(args.chars[1]))

    elif (len(args.chars) == 1):
        print('TOO FEW PARAMS')

    elif (len(args.chars) == 0):
        print('NO PARAMS')
    else:

        print('TOO MUCH PARAMS')
except ValueError:
    print("ValueError")
except IndentationError:
    print("IndentationError")
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except RuntimeError:
    print("RuntimeError")
