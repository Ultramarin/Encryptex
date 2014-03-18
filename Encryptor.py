# coding=utf-8
from random import randint
import random
import helpers

def user_diag_EK(max_int_const=26):
    """
    Инициирует диалог с пользователем. Для получения шифровочного ключа.
    Выполняет его проверку, в случае ввода ключа пользователем.
    Возвращает - готовый шифровочный ключ, размером 26 символом
    """
    question1 = 'Вы имеете ключ шифрования верхнего уровня? yes/no\n'
    question2 = 'Введите ключ шифрования верхнего уровня.\n'
    answer1 = 'Длина ключа шифрования должна быть равна %s символам, а так же должна состоять из A-Z' % max_int_const
    answer2 = "Сохраните сгенерированный ключ. Он необходим для дальнейшего дешифрования."
    encrypt_key = None

    def generate_new_encrypt_key(max_int_const=26):
        """
        Генерирует случайную последовательность букв - состоящую из английского алфавита.
        Длина каждой строки 13 букв - половина алфавита.
        В случае если slice не указан - функция даст на выходе строку из перемешанных букв английского алфавита.
        """
        input_ = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
        inputted_keys = input_.split(',')

        mixed_alfabet = random.sample(inputted_keys, max_int_const)
        encrypt_key = ''
        for x in mixed_alfabet:
            encrypt_key += x
        return encrypt_key.lower()

    def EK_check(encrypt_key, max_int_const=26):
        """
        Прооверяет ключ.
        :param encrypt_key:
        :param max_int_const:
        Правильно введенный ключ идентефицируется по следующим признакам:
        Длина 26 символов.
        Ключ состоит из латиницы.
        Ключ не содержит символов.
        Буквы в ключе не повторяются.

        """
        example_key = generate_new_encrypt_key()
        checker = ''

        for x in encrypt_key:
            if x in example_key:
                checker += x
        if len(checker) == max_int_const:
            return True
        else:
            return False

    while True:
        user_answer = raw_input(question1)
        if user_answer == 'yes':
            encrypt_key = raw_input(question2)
            if EK_check(encrypt_key):
                break
            else:
                print answer1
        elif user_answer == 'no':
            encrypt_key = generate_new_encrypt_key()
            print answer2
            break

    print "Ваш ключ '%s' был успешно сохранен." % encrypt_key
    return encrypt_key


def gen_x_y_list(input_text, tabname):
    """
    Генерирует список случайных координат,
    длина которого равна длине введенного текста
    """
    def generate_x_axis(tabname):
        #Генерирует случайную координату, в оси х. Для матрицы
        return randint(0, len(tabname) - 1)


    def generate_y_axis(tabname):
        #Генерирует случайную координату, в оси y. Для матрицы
        return randint(0, len(tabname[0]) - 1)


    coordinates_listXY = []
    input_text_length = len(input_text)
    while True:
        x_axis = generate_x_axis(tabname)
        y_axis = generate_y_axis(tabname)
        xy_axis = [x_axis, y_axis]
        if xy_axis not in coordinates_listXY:
            coordinates_listXY.append(xy_axis)
        if len(coordinates_listXY) == input_text_length:
            break

    return coordinates_listXY


def encrypt_text(input_text, coordinates_list, tab_name):
    """
    Раскидывает введенный текст - по матрице(используя сгенерированные верхней функцией координаты)
    """
    input_text = input_text
    counter = -1
    for x in coordinates_list:
        counter += 1
        tab_name[x[0]][x[1]] = input_text[counter]


def gen_decode_key(coordinates_list, encode_key):
    """
    Генерирует дешифровочный ключ(второй из ключей)
    """
    encode_key_x = encode_key[:13]
    encode_key_y = encode_key[13:]
    decode_key = ''

    for c in coordinates_list:
        x = encode_key_x[c[0]]
        y = encode_key_y[c[1]]
        decode_key += x + y

    return decode_key.decode('utf8')


def gen_encoded_text_string(tab_name):
    """
    Превращает матрицу в строку текста
    """
    encoded_text = ''

    for x in tab_name:
        encoded_text += "".join(x)

    return encoded_text


def user_diag(tabname):
    """
    Инициализация диалога с пользователем.
    В ходе которой - происходит шифрация введенного пользователем текста
    """
    question1 = u'Введите текст для шифрования.' \
                u' Текст должен состоять только из русских букв. Без использования символов \n'
    dk_enctext = (1, 2)
    answer1 = u"Ваш текст был успешно зашифрован. \n Дешифровочный ключ:\n %s \n Зашифрованный текст:\n %s "
    while True:
        text_to_encode = raw_input(question1)
        text_to_encode = text_to_encode.decode('utf8')
        text_to_encode = text_to_encode.upper()
        if helpers.key_in_alfabet(text_to_encode):
            coordinates_list = gen_x_y_list(text_to_encode, tabname)
            #Генерируем рандомный список координат, длиной - равной длине введенного текста.

            encrypt_text(text_to_encode, coordinates_list, tabname)
            #В случайном порядке - разбрасываем шифруемое слово по матрице.

            encode_key = user_diag_EK()
            #Вызываем генератор шифровального ключа.

            decode_key = gen_decode_key(coordinates_list, encode_key)
            #Вызываем генератор расшифровочного ключа.

            encoded_text_string = gen_encoded_text_string(tabname)
            #Вызываем декодер матрицы - в строку.


            dk_enctext = (decode_key, encoded_text_string)
            print answer1 % dk_enctext
            break


table = helpers.keytablegen()

user_diag(table)

