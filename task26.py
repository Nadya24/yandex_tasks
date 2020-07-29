# Выбор пароля
# Напишите программу, которая будет требовать у пользователя ввода
# нового пароля до тех пор, пока не будет введен корректный,
# либо пока пользователь не прекратит программу с клавиатуры,
# то есть нажмет комбинацию клавиш Ctrl-Break или аналогичную ей.
# Критерии правильности пароля аналогичны критериям из задачи
# "Пароли часть 2" из классной работы.
# Если пользовател вводит неправильный пароль,
#  то необходимо вывести имя класса того типа исключения,
#  который будет "выброшен" вашей программой. После этого ввод продолжается.
# Если пользователь прерывает работу программы "волшебной"
#  комбинацией клавиш, то надо вывести фразу
#  Bye-Bye и сразу же завершить работу программы.
# Если пользователь вводит текст Ctrl+Break, то программа
#  должна искусственно сымиттировать нажатие "волшебной" комбинации клавиш.
# Как только будет введен правильный пароль следует
#  вывести ok и тотчас же прекратить выполнение программы.

# Пример 1
# Ввод Вывод
# 12345
# amsndbashgdwgehd
# qweasdzxc1Z
# U1S6OTeEпьdъТ3
# LengthError
# LetterError
# SequenceError
# ok
# Пример 2
# Ввод Вывод
# abcd
# abcdefghyvb
# Abcdefghyvb8
# Ctrl+Break
# LengthError
# LetterError
# SequenceError
# Bye-Bye
# Пример 3
# Ввод Вывод
# Ctrl+Break
# Bye-Bye

keyboard_en = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
               'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
while 1:
    try:
        password = input("Введите пароль")
        # assert len(password) > 8, "error"
        if len(password) < 8:
            print("LengthError")
            continue
        if ((password == password.lower()) or (password == password.upper())):
            print("LetterError")
            continue
        a = False
        for i in range(10):
            if str(i) in password:
                a = True

        if not a:
            print("NumError")
            continue

        password = password.lower()

        b = True
        count_i = -1
        for j in range(5):
            count = 0
            for i, val in enumerate(keyboard_en[j]):
                if val in password:
                    count += 1

                else:
                    count = 0
                if count == 3:
                    b = False

        if not b:
            print("SequenceError")
            continue

        print("ok")
        break
    except KeyboardInterrupt:
        print("Bye-Bye")
        break
