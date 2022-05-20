# 6.3 Кортежи (tuple) и их методы

# кортеж - неизменяемый упорядоченный список
# синтаксис записи кортежа
a = 1, 2
print(a)

a = 1,
print(a)

a = (1, 2, 3)
b = tuple([2, 3, 4])
print(a)
print(b)

# операции распаковки коллекций
x, y, z = a
print(x, y, z)
a1, b1 = (1, 2)
print(a1, b1)
a2, b2 = [2, 3]
print(a2, b2)
a3, b3 = 'ra'
print(a3, b3)
a4, b4 = {'house': 'дом', 'ball': 'мяч'}
print(a4, b4)

# индексирование и срезы
print(len(a))
print(a[1:2])
print(a[:2])

# при полном срезе копия кортежей не создаются
b = a[:]
print(id(a), id(b))

# кортеж можно использовать в качестве ключа для словаря
# списки нельзя использовать в качестве ключей, т.к. список - это изменяемый тип
# d = {}
# d[a] = "кортеж"
d = {a: "кортеж"}
print(d)

# кортеж занимает меньше памяти, чем список
lst = [1, 2, 3]
a = (1, 2, 3)
print(lst.__sizeof__())
print(a.__sizeof__())

# создание пустого кортежа
a = ()
b = tuple()
# объединение кортежей, вложенные кортежи
a = a + (1,)
print(a)
a = (2, 3) + a
a += (("a", "hello"),)
print(a)

# формирование кортежей дублированием элементов
b = (0,) * 10
print(b)
b = ("hello", "world") * 5
print(b)

# удалять элементы кортежа нельзя
# del a[1]  # выдаст ошибку

# функция tuple - создает кортеж из любого итерируемого объекта
a = tuple([1, 2, 3])
print(a)
a = tuple("hello")
print(a)

# преобразование кортежа в список
s = list(a)
print(s)

# в кортеж можно вносить изменения только внутри элементов, которые являются изменяемыми типами данных
c = (True, [1, 2, 3], 'hello', 5, {"house": "дом"})
print(c)
print(c[1])
c[1].append("5")
print(c)

# подсчет количества указанных элементов в кортеже
a = ("abc", 2, [1, 2], True, 2, 5)
print(a.count("abc"))
print(a.count(2))
print(a.count("hello"))

# поиск элемента, возвращает индекс первого найденного элемента
print(a.index(2))
print(a.index(2, 2))
# print(a.index(2, 2, 3))  # поиск несуществующего элемента возвращает ошибку
a.index(2, 2, 5)

# проверка вхождения
print(3 in a)
print([1, 2] in a)

# Задачи
print("\n", "Задачи", sep='')

# # Task 3
# t = (3.4, -56.7)
# t += tuple(map(int, input().split()))
# print(t)

# Task 4
# cities = tuple(input().split())
# new_el = "Москва"
# if new_el not in cities:
#     cities += (new_el, )
# print(*cities)

# Task 5
# # Variant 1
# cities = tuple(input().split())
# cities2 = tuple(x for x in cities if x != 'Ульяновск')
# print(*cities2)
# # Variant 2
# print(*tuple(x for x in tuple(input().split()) if x != 'Ульяновск'))
# # Variant 3
# cities = tuple(input().split())
# if "Ульяновск" in cities:
#     idx = cities.index("Ульяновск")
#     cities = cities[:idx] + cities[idx+1:]
# print(*cities)

# Task 6
# st_names = tuple(input().lower().split())
# print(*(x for x in st_names if 'ва' in x))

# Task 7
# t1 = tuple(map(int, input().split()))
# t2 = tuple(x for i, x in enumerate(t1) if x not in t1[:i])
# print(*t2)

# Task 8
# t = tuple(map(int, input().split()))
# print(*(i for i, x in enumerate(t) if t.count(x) > 1))

# Task 9
# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N = int(input())
# t2 = tuple(t[i][:N] for i in range(N))
# for x in t2:
#     print(*x)

# Task 10
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# t = tuple(tuple(row.split()) for row in lst_in)
# print(t)

