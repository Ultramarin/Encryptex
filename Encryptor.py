# coding=utf-8
from random import randint
import random


def user_diag_EK(max_int_const=26):
    question1 = 'Вы имеете ключ шифрования верхнего уровня? yes/no\n'
    question2 = 'Введите ключ шифрования верхнего уровня.\n'
    answer1 = 'Длина ключа шифрования должна быть равна %s символам, а так же должна состоять из A-Z' % max_int_const
    answer2 = "Сохраните сгенерированный ключ. Он необходим для дальнейшего дешифрования."
    encrypt_key = None

    def generate_new_encrypt_key(max_int_const=26):
        """
        Генерирует случайную последовательность букв - состоящую из английского алфавита.
        slice - подать данные в виде - строки разбитой на два элемента, в составе списка.
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


def get_random_rus_letters(quantity=13):
    """
    Generate a n-length string of russian letters.
    """

    ruskey_list = []
    rus_alfabet_dict = {1: '\xd0\x90', 2: '\xd0\x91', 3: '\xd0\x92', 4: '\xd0\x93',
                        5: '\xd0\x94', 6: '\xd0\x95', 7: '\xd0\x81', 8: '\xd0\x96',
                        9: '\xd0\x97', 10: '\xd0\x98', 11: '\xd0\x99', 12: '\xd0\x9a',
                        13: '\xd0\x9b', 14: '\xd0\x9c', 15: '\xd0\x9d', 16: '\xd0\x9e',
                        17: '\xd0\x9f', 18: '\xd0\xa0', 19: '\xd0\xa1', 20: '\xd0\xa2',
                        21: '\xd0\xa3', 22: '\xd0\xa4', 23: '\xd0\xa5', 24: '\xd0\xa6',
                        25: '\xd0\xa7', 26: '\xd0\xa8', 27: '\xd0\xa9', 28: '\xd0\xaa',
                        29: '\xd0\xab', 30: '\xd0\xac', 31: '\xd0\xad', 32: '\xd0\xae',
                        33: '\xd0\xaf'}

    for x in xrange(quantity):
        #TODO: make it constant
        randletter = rus_alfabet_dict.get(randint(1, 33)).decode("utf8")
        ruskey_list.append(randletter)

    return ruskey_list


def keytablegen():
    keytable = []

    #TODO: make it constant
    for x in xrange(13):
        keytable.append(get_random_rus_letters())

    return keytable


def key_in_alfabet(key):
    rus = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
    rus = rus.decode('utf8')
    logical_key = ''
    for x in key:
        if x in rus:
            logical_key += x
    if len(logical_key) == len(key):
        return True
    else:
        return False


def print_board(var):
    for x in var:
        print " ".join(x)


def generate_x_axis(tabname):
    return randint(0, len(tabname) - 1)


def generate_y_axis(tabname):
    return randint(0, len(tabname[0]) - 1)


def gen_x_y_list(input_text, tabname):
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
    input_text = input_text
    counter = -1
    for x in coordinates_list:
        counter += 1
        tab_name[x[0]][x[1]] = input_text[counter]


def gen_decode_key(coordinates_list, encode_key):
    encode_key_x = encode_key[:13]
    encode_key_y = encode_key[13:]
    decode_key = ''

    for c in coordinates_list:
        x = encode_key_x[c[0]]
        y = encode_key_y[c[1]]
        decode_key += x + y

    return decode_key.decode('utf8')


def gen_encoded_text_string(tab_name):
    encoded_text = ''

    for x in tab_name:
        encoded_text += "".join(x)

    return encoded_text


def user_diag(tabname):
    question1 = u'Введите текст для шифрования.' \
                u' Текст должен состоять только из русских букв. Без использования символов \n'
    dk_enctext = (1, 2)
    answer1 = u"Ваш текст был успешно зашифрован. \n Дешифровочный ключ:\n %s \n Зашифрованный текст:\n %s "
    while True:
        text_to_encode = raw_input(question1)
        text_to_encode = text_to_encode.decode('utf8')
        text_to_encode = text_to_encode.upper()
        if key_in_alfabet(text_to_encode):
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


table = keytablegen()

user_diag(table)

print_board(table)
