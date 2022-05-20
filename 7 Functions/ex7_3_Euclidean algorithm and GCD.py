# 7.3 Алгоритм Евклида для нахождения НОД. Тестирование функций

import time


def get_nod1(a, b):
    """ Вычисляется НОД для натуральных чисел a и b
        по алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


def get_nod2(a, b):
    """ Вычисляется НОД для натуральных чисел a и b
        по быстрому алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def test_nod(func):
    # --- тест № 1 -----------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("#test 1 - ok")
    else:
        print("#test 1 - fail")

    # --- тест № 2 -----------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#test 2 - ok")
    else:
        print("#test 2 - fail")

    # --- тест № 3 -----------
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("#test 3 - ok")
        print("dt =", dt)
    else:
        print("#test 3 - fail")
        print("dt =", dt)


# res = get_nod1(18, 24)
# print(res)

help(get_nod1)
test_nod(get_nod1)
test_nod(get_nod2)
