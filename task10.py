# Форматирование файла
# Очень часто данные, которые мы получаем, очень большие,
# и их приходится форматировать.
# Попробуйте написать программу, которая форматирует
# текстовый файл и выводит его содержимое в указанных рамках.
# Программа принимает на вход высоту, ширину (--frame-height,
# —frame-width) блока в символах и имя файла,
# а на выходе выводит содержимое (начальную часть)
#  файла которое помещается в указанные размеры.
# Если строка не умещается по длине, то ее нужно перенести.


# Вся логика форматирования должна быть реализована в функции
# format_text_block(frame_height, frame_width, ﬁle_name),
# которая возвращает отформатированный текст и в
# дальнейшем может быть использована в других скриптах.

# В случае возникновения ошибок при работе с файлом необходимо
# вернуть текст исключения, которое выбрасывается в этой ситуации.
# Пример 1
# Ввод Вывод
# python3 solution.py —frame-height 10 —frame-width 30 filename.txt
# Chapter I: An Unexpected Party
# In a hole in the ground thereсссссссссссссссссссссссссс
# lived a hobbit. Not a nasty, d
# irty, wet hole, filled with th
# e ends of worms and an oozy sm
# ell, nor yet a dry, bare, sand
# Пример 2
# Ввод Вывод
# python3 solution.py —frame-height 10 —frame-width 30 file.txt
# [Errno 2] No such file or directory: 'file.txt'
# Примечания
# Тестирующая система будет как вызывать вашу программу,
# так и подключать ее к другому скрипту с помощью import.

# Файл, используемый для проверки.

# Библиотека argparse опять же обязательна к использованию.


import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, 'r') as f:
            res = f.read()
        result = ''
        count = 1
        count_sn = 0
        fw = 0
        for i in res:
            if i == '\n':
                count_sn += 1
                if fw == 1:
                    result = result[:-1]
                    frame_height += 1
                    fw = 0

            if count_sn > 1:
                result += '\n'
                frame_height -= 1
                count = 1
                if frame_height == 0:
                    print(result[:-1])

            if i != '\n':
                fw = 0
                count_sn = 0
                result += i
                if count == frame_width:
                    result += '\n'
                    frame_height -= 1
                    count = 1
                    fw = 1
                else:
                    count += 1
            if frame_height == 0:
                print(result[:-1])

    except FileNotFoundError as e:
        print(e)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--frame-height', nargs='?',
                        type=int)
    parser.add_argument('--frame-width', nargs='?',
                        type=int)
    parser.add_argument('filename')

    args = parser.parse_args()
    format_text_block(args.frame_height, args.frame_width,
                      args.filename)
    # if mess:
    #     print(mess)


if __name__ == "__main__":
    main()
