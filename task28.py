# Характерные ошибки с паролями
# Вам доступны файл с наиболее частыми паролями и файл-словарь слов английского языка.
# Для решения задачи вы можете скачать эти файлы по ссылке.


# Проверьте все пароли в указанном списке на сооответствие следующим правилам:
# Пароль должен состоять из более, чем 8 символов – если не так, то возбуждайте исключение LengthError.
# В пароле должны присутствовать большие и маленькие буквы любого алфавита
# – если не так, то возбуждайте исключение LetterError.
# В пароле должна быть хотя бы одна цифра – если не так, то возбуждайте исключение DigitError.
# В пароле не должно быть ни одной комбинации из 3 буквенных символов,
# стоящих рядом в клавиатурном ряду, независимо от того, русская раскладка или английская,
#  например, недопустимы «йцу», «hjk» и т.д. – если не так, то возбуждайте исключение SequenceError.
# В пароле должны отсутствовать словарные слова – если не так, то возбуждайте исключение WordError.
# Сделайте класс ошибок в пароле PasswordError, унаследуйте от него классы для каждого случая.
# Соберите статистику о том, какое количество и каких ошибок встречается в
# приведенном списке паролей и выведите эту информацию в следующем виде:
# Exception1 - Количество1
# Exception2 - Количество2
# ...
# ExceptionN - КоличествоN
# Подумайте, как лучше поступить со случаем, если пароль
# не соответствует нескольким критериям одновременно?
# Выводите исключения в алфавитном порядке.
#
#

list_password = ['qwe35mfniD', '123456789876', 'rntjdjvbenscp',
                 'Wndmgbax4567a', 'Pzswbtd123', '123', '23', 'password']


class PasswordError:
    def __init__(self):
        self.err_length = 0
        self.err_letter = 0
        self.err_digit = 0
        self.err_sequence = 0
        self.err_word = 0


class LengthError(PasswordError):
    def __init__(self):
        super().__init__()

    def check_length(self, some_str):
        if len(some_str) < 8:
            self.err_length += 1


class LetterError(PasswordError):
    def __init__(self):
        super().__init__()

    def check_letter(self, some_str):
        if ((some_str == some_str.lower()) or (some_str == some_str.upper())):
            self.err_letter += 1



class DigitError(PasswordError):
    def __init__(self):
        super().__init__()

    def check_digit(self, some_str):
        a = False
        for i in range(10):
            if str(i) in some_str:
               a = True
        if not a:
            self.err_digit += 1


class SequenceError(PasswordError):
    def __init__(self):
        super().__init__()

    def check_sequence(self, some_str):
        some_str = some_str.lower()
        keyboard_en = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
               'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
        b = True
        count_i = -1
        pre_str = None
        for j in range(5):
            count = 0
            for indx, value in enumerate(some_str):
                for i, val in enumerate(keyboard_en[j]):
                    if value == val:
                        if not pre_str:
                            pre_str = i
                            count += 1
                        elif i-1 == pre_str:
                            count += 1
                            pre_str = i
                        else:
                            count = 0
                    if count >= 3:
                        b = False

        if not b:
            self.err_sequence += 1


class WordError(PasswordError):
    def __init__(self):
        super().__init__()

    def check_word(self, some_str):
        list_word = ['password','pass','пароль']
        err = False
        for i in list_word:
            if i in some_str:
                err = True
        if err:
            self.err_word += 1


len_err = LengthError()
letter_err = LetterError()
digit_err = DigitError()
sequence_err = SequenceError()
word_err = WordError()

for i in list_password:
    len_err.check_length(i)
    letter_err.check_letter(i)
    digit_err.check_digit(i)
    sequence_err.check_sequence(i)
    word_err.check_word(i)


print("DigitError - %s" % digit_err.err_digit)
print("LengthError - %s" % len_err.err_length)
print("LetterError - %s" % letter_err.err_letter)
print("SequenceError - %s" % sequence_err.err_sequence)
print("WordError - %s" % word_err.err_word)
