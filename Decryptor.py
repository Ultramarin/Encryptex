import helpers
# coding=utf-8
def user_diag_encripted_text():
    """
    Инициирует диалог с пользователем. Для получения зашиврованого текста.
    Выполняет его проверку, в случае ввода пользователем правильно текста то
    Возвращает зашиврований текст, размером 169 символов
    """
    while True:
    ET = raw_input('Введите зашиврований текст')
    if len(ET) == 169 and helpers.key_in_alfabet() :
        break
    else:
        print ('Даный текст не верен проверте вводимый текст')

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

def matrix():
"""Создает матрицу из строки вводимой пользывтелем"""
    ETR = user_diag_EK_decrypt()
    list0 = []
    matr = []
    list1 = []
    caunter = 0
    for x in ETR:
        list.append(x)

    for x in xrange(2):
        for x in xrange(13):
            list1.append(list[caunter])
            caunter = caunter+1
            matr.append(list1)
    return matr

def decript():
    Encmatrix = matrix()
    cordinets = EK_parser()
    for x in cordinets:
        enct = enct + Encmatrix[cordinets[0]][cordinets[1]]

    return enct
