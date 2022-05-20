# 6.1 Введение в словари

d = {"house": "дом", "car": "машина",
     "tree": "дерево", "road": "дорога",
     "river": "река"}
print(d)

# при обращении к словарю надо прописывать только существующие ключи
print(d["house"])

# при использовании функции dict в качестве имен ключей можно использовать только разрешенные имена переменных
# они преобразуются в строки
d1 = dict(one=1, two=2, three='3', four='4')
print(d1)

# использование dict для преобразования списков
lst = [[2, "неудовлетворительно"], [3, "удовлетворительно"], [4, "хорошо"], [5, "отлично"]]
print(lst)
d2 = dict(lst)
print(d2)
d3 = dict()
d4 = {}

# в качестве ключей можно использовать любые неизменямые типы данных
# определение новых ключей добавляет их в словарь
# список не может быть ключом
d[True] = 'Истина'
d[False] = 'Ложь'
print(d)

# присваивание по существующему ключу меняет его значение
d3[True] = 'Истина'
d3[False] = 'Ложь'
print(d3)
d3[True] = 1
print(d3)

# список может быть значением
d4 = {True: 1, False: "Ложь", 'list': [1, 2, 3], 5: 5}
print(d4)

# функции словаря
print(len(d))
del d[True]
print("abc" in d)
# проверка проводится только в ключах, а не в значениях
# обратная проверка
print("abc" not in d)

# Примеры задания ключей
d[True] = 'истина'
d[1] = 'one'
d['dict'] = {'one': 1, 'two': 2}
d[5.6] = 5.6
d["house"] = ['дом', 'жилище', 'хижина']
print(d)

# Задачи
print("\n", "Задачи", sep='')

# Task 3
# # Variant 1
# lst = [x.split('=') for x in input().split()]
# for i in range(len(lst)):
#     lst[i][1] = int(lst[i][1])
# d = dict(lst)
# print(*sorted(d.items()))
# # Variant 2
# d = dict(c.split('=') for c in input().split())
# for c in d:
#   d[c] = int(d[c])
# print(*sorted(d.items()))
# # Variant 3
# lst_in = input().split()
# lst = [[i.split('=')[0], int(i.split('=')[1])] for i in lst_in]
# d = dict(lst)
# print(*sorted(d.items()))
# # Variant 4 - тоже неплохо
# s = input().split()
# d = {}
# for x in s:
#     x = x.split('=')
#     d[x[0]] = int(x[1])
# print(*sorted(d.items()))
# # Variant 5 - top
# lst = [i.split('=') for i in input().split()]
# d = {i: int(v) for i, v in lst}
# print(*sorted(d.items()))

# Task 4
# # Variant 1
# import sys
# # считывание списка из входного потока
# lst_in = [x.split('=') for x in map(str.strip, sys.stdin.readlines())]
# d = {int(k): v for k, v in lst_in}
# print(*sorted(d.items()))
# # Variant 2 - Zen of Python
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for i in lst_in:
#     key, value = i.split('=')
#     d[int(key)] = value
# print(*sorted(d.items()))
# # Variant 3
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {int(x.split('=')[0]): x.split('=')[1] for x in lst_in}
# print(*sorted(d.items()))

# Task 5
# # Variant 1
# lst = input().split()
# d = {}
# for x in lst:
#     k, v = x.split('=')
#     d[k] = v
# if 'house' in d and 'True' in d and '5' in d:
#     print('ДА')
# else:
#     print('НЕТ')
# # Variant 2
# d = dict([i.split('=') for i in input().split()])
# print('ДА' if 'house' in d and 'True' in d and '5' in d else 'НЕТ')

# Task 6
# d = dict([x.split('=') for x in input().split()])
# sel_keys = ['False', '3']
# for i in sel_keys:
#     if i in d:
#         del d[i]
# print(*sorted(d.items()))

# Task 7
# # Variant 1 - excessive split
# lst = input().split()
# d = {}
# for x in lst:
#     d[x[0:2]] = ['+' + x[2:]] if x[0:2] not in d else d[x[0:2]] + ['+' + x[2:]]
# print(*sorted(d.items()))
# # Variant 2
# lst = input().split()
# d = {}
# for x in lst:
#     d[x[0:2]] = [x] if x[0:2] not in d else d[x[0:2]] + [x]
# print(*sorted(d.items()))

# Task 8
# # пример из https://www.guru99.com/python-dictionary-append.html
my_dict = {"Name": [], "Address": [], "Age": []}
my_dict["Name"].append("Guru")
my_dict["Address"].append("Mumbai")
my_dict["Age"].append(30)
print(my_dict)
# # Variant 1
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(lst_in)
# lst = [s.split() for s in lst_in]
# print(lst)
# d = {}
# for line in lst:
#     if line[1] in d:
#         d[line[1]].append(line[0])
#     else:
#         d[line[1]] = [line[0]]
# print(*sorted(d.items()))
# # Variant 2
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for i in lst_in:
#     value, key = i.split()
#     if key in d:
#         d[key] += [value]
#     else:
#         d[key] = [value]
# print(*sorted(d.items()))

# Task 9
# # Variant 1
# d = {}
# while True:
#     x = int(input())
#     if x == 0:
#         break
#     elif x in d:
#         print(f'значение из кэша: {d[x]}')
#     else:
#         d[x] = round(x ** 0.5, 2)
#         print(d[x])
# # Variant 2
# n = int(input())
# d = {}
# while n != 0:
#     if n in d:
#         print(f'значение из кэша: {d[n]}')
#     else:
#         d[n] = round(n ** .5, 2)
#         print(d[n])
#     n = int(input())

# Task 10
# # Variant 1
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for s in lst_in:
#     if s in d:
#         print(f'Взято из кэша: {d[s]}')
#     else:
#         d[s] = "HTML-страница для адреса " + s
#         print(d[s])
# # Variant 2 - f-строки используются не только в принте
# import sys
# d = {}
# for addr in list(map(str.strip, sys.stdin.readlines())):
#     if addr in d:
#         print(f'Взято из кэша: {d[addr]}')
#     else:
#         d[addr] = f'HTML-страница для адреса {addr}'
#         print(d[addr])

