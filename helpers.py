# coding=utf-8
from random import randint


def keytablegen(quantity=13, max_int=33, min_int=1):
    def get_random_rus_letters(quantity, max_int, min_int):
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
            randletter = rus_alfabet_dict.get(randint(min_int, max_int)).decode("utf8")
            ruskey_list.append(randletter)

        return ruskey_list


    keytable = []

    for x in xrange(quantity):
        keytable.append(get_random_rus_letters())

    return keytable


def print_board(var):
    """
    Печатает матрицу
    """
    for x in var:
        print " ".join(x)


def key_in_alfabet(key):
    """
    Проверяет вводимый текст на принадлежность к русскому алфавиту.
    В противном случае возвращет False

    """
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

