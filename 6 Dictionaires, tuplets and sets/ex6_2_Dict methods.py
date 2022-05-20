# 6.2 Методы словаря. Перебор его элементов в цикле

# dict.fromkeys(список[, значение по умолчанию]
# создает словарь с ключами из списка, может присвоить им значения по умолчанию
lst = ["+7", "+6", "+5", "+4"]
a = dict.fromkeys(lst)
print(a)

a1 = dict.fromkeys(lst, "код страны")
print(a1)

# очистка
a.clear()
print(a)

# копия
d = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 5}
print(d)
d2 = d.copy()
d2["list"] = [5, 6, 7]
print(id(d2), d2)
print(id(d), d)

# get
print(d.get("list"))  # возвращает значение указанного ключа
print(d.get("несуществующий ключ"))  # для несуществующего ключа возвращает значение None
print(d.get("несуществующий ключ", False))  # для несуществующего ключа возвращает указанное значение False

# setdefault - возвращает значение ключа, а если он отсутствует, создает новый ключ
print("\n", "Setdefault", sep='')
print(d.setdefault("list"))
print(d.setdefault(3))  # возвращает значение None и создает новый ключ 3
print(d)
print(d.setdefault(3))
del d[3]
print(d.setdefault(3, "three"))
print(d)

# pop
print("\n", "Метод pop", sep='')
print(d.pop(3))
print(d)
print(d.pop("abc", False))  # возвращает указанное значение, если ключ не найден
# popitem
d.popitem()  # удаляет последнюю запись
d.popitem()
# popitem от пустого словаря возвращает ошибку

# keys
print("\n", "Метод keys", sep='')
print(d.keys())
d = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 5}
print(d.keys())
for x in d:
    print(x)

# values
print("\n", "Метод values", sep='')
print(d.values())
for x in d.values():
    print(x)

# items
print("\n", "Метод items", sep='')
print(d.items())  # возвращает список кортежей
for x in d.items():
    print(x)  # возвращает кортежи

# кортежи
print("\n", "Кортежи", sep='')
x, y = (1, 2)
print(x, y)
for key, value in d.items():
    print(key, value)

# update
print("\n", "Update / Обновление словаря", sep='')
d = dict(one=1, two=2, three="3", four="4")
print(d)
d2 = {2: "неуд", 3: "удовл", 'four': "хор", 5: "отл"}
print(d2)
d.update(d2)  # значение совпадающие ключей заменяются, новые ключи и значения добавляются
print(d)

# объединение словарей
print("\n", "Объединение словарей", sep='')
d = dict(one=1, two=2, three="3", four="4")
d3 = {**d, **d2}  # значения из второго словаря замещают значения в первом (по совпадающим ключам)
print(d3)
d3 = {**d2, **d}  # можно объединять два и более словаря
print(d3)
d4 = d | d2  # альтернативный вариант объединения словарей, появился в Python 3.9
print(d4)

# Задачи
print("\n", "Задачи", sep='')

# >>> import unicodedata
# >>> unicodedata.name("\xa0")
# 'NO-BREAK SPACE'
# >>> unicodedata.name("\x20")
# 'SPACE

# Task 3
# Variant 1
# morze = dict(А='.-', М='--', Ш='----',
#              Б='-...', Н='-.', Щ='--.-',
#              В='.--', О='---', Ъ='--.--',
#              Г='--.', П='.--.', Ы='-.--',
#              Д='-..', Р='.-.', Ь='-..-',
#              Е='.', Ё='.', С='...', Э='..-..',
#              Ж='...-', Т='-', Ю='..--',
#              З='--..', У='..-', Я='.-.-',
#              И='..', Ф='..-.',
#              Й='.---', Х='....',
#              К='-.-', Ц='-.-.',
#              Л='.-..', Ч='---.')
# morze[' '] = '-...-'
# str1 = input().upper()
# lst = []
# for s in str1:
#     lst.append(morze[s])
# print(*lst)
# # Variant 2
# morze = dict(А='.-', М='--', Ш='----',
#              Б='-...', Н='-.', Щ='--.-',
#              В='.--', О='---', Ъ='--.--',
#              Г='--.', П='.--.', Ы='-.--',
#              Д='-..', Р='.-.', Ь='-..-',
#              Ё='.', Е='.',  С='...', Э='..-..',
#              Ж='...-', Т='-', Ю='..--',
#              З='--..', У='..-', Я='.-.-',
#              И='..', Ф='..-.',
#              Й='.---', Х='....',
#              К='-.-', Ц='-.-.',
#              Л='.-..', Ч='---.')
# morze[' '] = '-...-'
# # print(*[morze[x] for x in input().upper()])
#
# # Task 4
# # Variant 1
# rmorze = {v: k for k, v in morze.items()}
# for x in input().split():
#     print(rmorze[x].lower(), end='')
# # Variant 2
# morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..', 'и': '..',
#          'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...',
#          'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-',
#          'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-···-'}
# back_morze = {v: k for k, v in morze.items()}
# print(*(back_morze[code] for code in input().lower().split()), sep='')

# Task 5
# print(*dict.fromkeys(input().split()))

# Task 6
# # import timeit
# # # Version 1
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # code_to_test1 = """
# # lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
# d = {}
# for x in lst_in:
#     k, v = x.split()
#     d[k] = d.setdefault(k, []) + [v]
# for key, value in d.items():
#     print(key, end=': ')
#     print(*value, sep=', ')
# # """
# # elapsed_time1 = timeit.timeit(code_to_test1, number=10000)/10000
# # # Version 2
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # code_to_test2 = """
# # lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
# d = {}
# for x in lst_in:
#     k, v = x.split()
#     d.setdefault(k, []).extend([v])
# #   d[k] = d.get(k, []) + [v]
# for key, value in d.items():
#     print(key, end=': ')
#     print(*value, sep=', ')
# # """
# # elapsed_time2 = timeit.timeit(code_to_test2, number=10000)/10000
# # # Version 3 - the best, most optimal and Zen
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # code_to_test3 = """
# # lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
# d = {}
# for x in lst_in:
#     k, v = x.split()
#     d.setdefault(k, []).append(v)
# for key, value in d.items():
#     print(key, end=': ')
#     print(*value, sep=', ')
# # """
# # elapsed_time3 = timeit.timeit(code_to_test3, number=10000)/10000
# # # Version 4 - defaultdic, f-string
# import sys
# from collections import defaultdict
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # code_to_test4 = """
# # from collections import defaultdict
# # lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
# d = defaultdict(list)
# print(*d)
# for x in lst_in:
#     k, v = x.split()
#     d[k].append(v)
# for key, value in d.items():
#     print(f"{key}: {', '.join(value)}")
# # """
# # elapsed_time4 = timeit.timeit(code_to_test4, number=10000)/10000
# # print('Variant 1 =', elapsed_time1)
# # print('Variant 2 =', elapsed_time2)
# # print('Variant 3 =', elapsed_time3)
# # print('Variant 4 =', elapsed_time4)

# Task 7
# # Variant 1
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# N = int(input()) * 1000
# # print(sorted(things, key=things.get, reverse=True))
# # min_wt = min(things.values())
# # print(min_wt)
# # s = 0
# for x in sorted(things, key=things.get, reverse=True):
#     if things[x] <= N:
#         # print(x, things[x], sep='-', end=' ')
#         print(x, end=' ')
#         N -= things[x]
# #         s += things[x]
# # print('\n', 'Итого вес:', s)
# Variant 2 - мой, без служебных комментов
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
N = int(input()) * 1000
for x in sorted(things, key=things.get, reverse=True):  # сортировка словаря по значениям
    if things[x] <= N:
        print(x, end=' ')
        N -= things[x]

