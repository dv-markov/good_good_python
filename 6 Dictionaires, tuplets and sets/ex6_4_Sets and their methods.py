# 6.4 Множества (set) и их методы

# Множество (set) - неупорядоченная коллекция уникальных элементов
# Множество - изменяемый тип данных

a = {1, 2, 3, "hello"}
print(a)
print(type(a))

# множество автоматически отбрасывает все дубли
a = {1, 2, 3, "hello", 2, 3, "hello"}
print(a)

# элементами множества могут быть только неизменяемые типы данных
# числа, булевы значения, строки, кортежи
# нельзя использовать списки, словари, другие множества
a = {1, 4.5, "hi", (4, True)}
print(a)

b = set()
print(b)
# фигурные скобки по умолчанию создают только словари
b = {}
print(b, type(b))

# Множества из итерируемого объекта
c = set([1, 2, 1, 0, 1, -1, 2])
# идентично
#  c = {1, 2, 1, 0, 1, -1, 2}
print(c)
d = set("abrakadabra")
print(d)
e = set(range(7))
print(e)
# обратиться к элементу множества по индексу невозможно
cities = ["Калуга", "Краснодар", "Тюмень", "Ульяновск", "Москва", "Тюмень", "Калуга", "Ульяновск"]
print(cities)
q = set(cities)
print(q)
print(list(q))

# перебор элементов множества
# множество - итерируемый, но не упорядоченный объект
for c in q:
    print(c)
print(len(q))
print("Москва" in cities)
print("abc" in cities)

# Методы для добавления и удаления элементов множества
b = set()
print(b)
# добавление одного элемента
b.add(7)
print(b)
b.add(7)
print(b)
b.add(3)
print(b)

# добавление нескольких элементов, любого итерируемого объекта
b.update(["a", "b", (1, 2)])
print(b)
b.update("abrakadabra")
print(b)

# удаление значения из множества
b.discard(2)  # удаление указанного элемента методом discard
b.discard(3)  # удаление несуществующего элемента не возвращает ошибку
print(b)
b.remove(7)  # удаление указанного элемента методом remove
print(b)  # удаление несуществующего элемента этим способом возвращает ошибку

print(b.pop())  # удаление произвольного элемента с возвратом значения
print(b.pop())  # pop из пустого множества приведет к ошибке
print(b.pop())
print(b)

b.clear()  # удаление всех элементов множества

# Задачи
print("\n", "Задачи", sep='')

# Task 3
# можно сортировать неупорядоченный тип данных перед выводом, при этом создается список
# s = set(map(float, input().split()))
# print(*sorted(s))

# Task 4
# s = set(input().lower().split())
# print(len(s))

# Task 5
# # Variant 1
# s = set(x for x in input() if x.isdigit())
# print(' '.join(sorted(s)) if s else "НЕТ")
# # Variant 2
# t = set(int(i) for i in input() if i.isdigit())
# print(*sorted(t) if t else ['НЕТ'])
# # Variant 3
# x = {c for c in input() if c.isdigit()}
# print([' '.join(sorted(x)), 'НЕТ'][len(x) == 0])
# # Variant 4
# print(*sorted(set(int(c) for c in input() if c.isdigit())) or ['НЕТ'])

# Task 6
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(len(set(lst_in)))

# Task 7
# # Variant 1
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# s = set()
# for x in lst_in:
#     s.add(x[:(x.find(":"))])
# print(len(s))
# # Variant 2
# s = {x[:(x.index(":"))] for x in lst_in}
# print(len(s))
# # Variant 3
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(len(set(i.split(":")[0] for i in lst_in )))

# Task 8
# # Variant 1
# s = set()
# c = input()
# while c != "q":
#     s.add(c)
#     c = input()
# print(len(s))
# # Variant 2 - итератор будет крутить функцию input, пока не найдет значение 'q'
# print(len(set(iter(input, 'q'))))
