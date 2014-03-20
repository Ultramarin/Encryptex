import helpers
# coding=utf-8
def user_diag_encripted_text():
    """
    Инициирует диалог с пользователем. Для получения зашыврованого текста.
    Выполняет его проверку, в случае ввода пользователем правильно текста то
    Возвращает зашыврований текст , размером 169 символов
    """
    while True:
        ET = raw_input('Введите зашыврований текст')
        if len(ET) > 169 and ET not in helpers.keytablegen(ET, leng='eng'):
            print ('')
        else:
            break

    return ET


def user_diag_EK_decrypt(max_int_const=26):
    """
    Инициирует диалог с пользователем. Для получения шифровочного ключа.
    Выполняет его проверку, в случае ввода ключа пользователем.
    Возвращает - готовый шифровочный ключ, размером 26 символом
    """
    question1 = 'Введите ключ шифрования верхнего уровня.\n'
    answer1 = 'Длина ключа шифрования должна быть равна %s символам, а так же должна состоять из A-Z' % max_int_const
    encrypt_key = None

    while True:
        user_answer = raw_input(question1)

        if helpers.EK_check(encrypt_key):
            break
        else:
            print answer1

    return encrypt_key


def user_diag_encode_key(lang='eng', const=338):
    while True:
        encode_key = raw_input('Введите дешифровочный ключ(вторичный)')
        if len(encode_key) > const or encode_key not in helpers.key_in_alfabet(encode_key, lang):
            print ('Дешифровочный ключ не верен')
        else:
            break


def EK_parser():
    """
    Переобразования дешифровачного ключа  вводимого пользователем в лист кординат
    зашифрованого текста
    """
    encrypt_key = user_diag_EK_decrypt()
    encrypt_key_x = encrypt_key[:13]
    encrypt_key_y = encrypt_key[13:]
    encrypt_key_dict = {}
    encode_key = user_diag_encode_key()
    encode_key_list_xy = []
    cordinates_list_letter = []
    cantor = 0
    coordinates_list = []

    while cantor <= len(encode_key):
        encode_key_x = encode_key[cantor]
        encode_key_y = encode_key[cantor + 1]
        encode_key_list_xy.append(encode_key_x)
        encode_key_list_xy.append(encode_key_y)
        cordinates_list_letter.append(encode_key_list_xy)
        cantor += 1

    cantor = 0

    for x in encrypt_key_x:
        encrypt_key_dict[x] = cantor
        cantor += 1

    cantor = 0
    encode_key_list_xy = []

    for x in encrypt_key_y:
        encrypt_key_dict[cantor] = x
        cantor += 1

    for x in cordinates_list_letter:
        x_coordinated = encrypt_key_dict[x[0]]
        y_coordinated = encrypt_key_dict[x[1]]
        encode_key_list_xy.append(x_coordinated)
        encode_key_list_xy.append(y_coordinated)
        coordinates_list.append(encode_key_list_xy)

    return coordinates_list
