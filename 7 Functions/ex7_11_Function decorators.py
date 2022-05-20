# 7.11 Декораторы функций

import time


print("""
# базовый вариант """)


def func_decorator(func):
    def wrapper():
        print("----------- что-то делаем перед вызовом функции -----------")
        func()
        print("----------- что-то делаем после вызова функции -----------")

    return wrapper


def some_func():
    print("Вызов функции some_func")


some_func()

f = func_decorator(some_func)
f()

some_func = func_decorator(some_func)
some_func()


print("""
# добавление аргументов """)


def func_decorator1(func):
    def wrapper(title):
        print("----------- что-то делаем перед вызовом функции -----------")
        func(title)
        print("----------- что-то делаем после вызова функции -----------")

    return wrapper


def some_funk1(title):
    print(f"Вызов функции some_func, title =", title)


some_funk1 = func_decorator1(some_funk1)
some_funk1('Тоже неплохо')


print("""
# универсальный метод для любых функций """)


def func_decorator2(func):
    def wrapper(*args, **kwargs):
        print("----------- что-то делаем перед вызовом функции -----------")
        res = func(*args, **kwargs)
        print("----------- что-то делаем после вызова функции -----------")
        return res

    return wrapper


def some_funk2(title, tag):
    print(f"Вызов функции some_func, title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"


some_funk2 = func_decorator2(some_funk2)
res1 = some_funk2('Python навсегда', 'h1')
print(res1)


print("""
# пример применения - тестировщик времени хода (универсальный): """)


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы {func}: {dt} сек")
        return res

    return wrapper


@test_time
def get_nod(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a


# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)

res1 = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)

print(res1, res2)


# Задачи
print("\n", "Задачи", sep='')


# Task 1
def func_show(func):
    def wrapper(*args, **kwargs):
        print(f"Площадь прямоугольника: {func(*args, **kwargs)}")

    return wrapper


@func_show
def get_sq(width, height):
    return width * height


get_sq(8, 11)


# Task 2

# Variant 1 - posted to stepik
print("""
# Вариант 1
# Принт внутри функции 
""")


def show_menu(func):
    def wrapper(*args):
        [print(f"{i+1}. {x}") for i, x in enumerate(func(*args))]
    return wrapper


@show_menu
def get_menu(s):
    return s.split()


get_menu('Главная Добавить Удалить Выйти')


# Variant 2
def show_menu2(func):
    def wrapper(*args, typ=0):
        return (tuple, list)[typ == 0](f"{i+1}. {x}" for i, x in enumerate(func(*args)))
    return wrapper


@show_menu2
def get_menu2(s):
    return s.split()


m2 = 'Главная Добавить Удалить Выйти'
print("""
# Преобразование строки меню в нумерованный список
# вывод через цикл
""")
for x in get_menu2(m2):
    print(x)

print("""
# Преобразование строки меню в нумерованный список
# вывод через через функцию join
""")
print('\n'.join(get_menu2(m2, typ=2)))


# Task 3

# # Variant 1
# def get_srt(func):
#     def wrapper(*args):
#         return sorted(func(*args))
#     return wrapper
#
#
# @get_srt
# def get_list(ls):
#     return list(map(int, ls.split()))
#
#
# print(*get_list(input()))
#
#
# # Variant 2
# def show_sorted(func):
#     return lambda *args, **kwargs: sorted(func(*args, **kwargs))
#
#
# @show_sorted
# def get_list(s):
#     return list(map(int, s.split()))
#
#
# print(*get_list(input()))


# Task 4

# Variant 1 - мой, без zip-функции
# def dictionize(func):
#     def wrapper(*args):
#         l1, l2 = func(*args)
#         l1len, l2len = len(l1), len(l2)
#         return {l1[i]: l2[i] for i in range(l1len if l1len < l2len else l2len)}
#     return wrapper
#
#
# @dictionize
# def str2list(str1, str2):
#     return str1.split(), str2.split()
#
#
# s1, s2 = input(), input()
# d = str2list(s1, s2)
# print(*sorted(d.items()))


# # Variant 2 - Timohin
# def sort_list(fn):
#     def wropper(*args):
#         return {key: value for key, value in zip(*fn(*args))}
#     return wropper
#
#
# @sort_list
# def get_list(s1, s2):
#     return (s1.split(), s2.split())
#
#
# s1, s2 = input(), input()
# d = get_list(s1, s2)
# print(*sorted(d.items()))

# # Variant 3 - Glozman
# def show_sorted(func):
#     return lambda *args, **kwargs: dict(zip(*func(*args, **kwargs)))
#
#
# @show_sorted
# def get_lists(s1, s2):
#     return s1.split(), s2.split()
#
#
# print(*sorted(get_lists(input(), input()).items()))


# Task 5

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def clear_extra_dashes(func):
    def wrapper(*args):
        return "-".join(func(*args).replace('-', ' ').split())
    return wrapper


@clear_extra_dashes
def get_slug(s):
    lst = ["-" if char in ": ;.,_" else t.get(char, char) for char in s.lower()]
    return "".join(lst)


# s = input()
s = 'Python - это круто!'
print(get_slug(s))


def test_time2(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = 0
        for i in range(100000):
            res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы {func}: {dt} сек")
        return res

    return wrapper


tt1 = test_time2(get_slug)
print(tt1(s))


# # Variant 2 - Timohin
# def del_dash(fn):
#     def wropper(s):
#         s = fn(s)
#         while '--' in s:
#             s = s.replace('--', '-')
#         return s
#     return wropper
#
#
# @del_dash
# def ru_en(s):
#     st = ''
#     for i in s:
#         if i in t:
#             st += t[i]
#         elif i in ": ;.,_":
#             st += '-'
#         else:
#             st += i
#     return st
#
#
# tt2 = test_time2(ru_en)
# print(tt2(s))


# # Varaint 3 - Glozmann
# import re
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# def hyphenator(func):
#     return lambda *args, **kwards: re.sub(r'-+', '-', func(*args, **kwards))
# @hyphenator
# def transliterate(s):
#     return s.lower().translate(str.maketrans({**t, **dict.fromkeys(': ;.,_', '-')}))
# print(transliterate(input()))
