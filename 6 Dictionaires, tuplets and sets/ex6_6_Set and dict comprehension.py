# 6.6 Генераторы множеств и словарей

# [<способ формирования значения> for <счетчик> in <итерируемый объект>]

# генератор списков
a = [x ** 2 for x in range(1, 5)]
print(a)

# генератор множеств
a = {x ** 2 for x in range(1, 5)}
print(a)

# генератор словарей
a = {x: x ** 2 for x in range(1, 5)}
print(a)

# генератор словарей/множеств работает гораздо быстрее, чем обычный цикл
d = [1, 2, '1', '2', -4, 3, 4]
# генератор
a = {int(x) for x in d}
print(a)
# обычный цикл
set_d = set()
for x in d:
    set_d.add(int(x))
print(set_d)

# генератор словаря
m = {"неуд": 2, "удовл": 3, "хорошо": '4', "отлично": '5'}
a = {key.upper(): int(value) for key, value in m.items()}
print(a)

# условия в генераторе множеств и словарей
d = [1, 2, '1', '2', -4, 3, 4]
a = {int(x) for x in d if int(x) > 0}
print(a)

m = {"безнадежно": 0, "убого": 1, "неудовлетворительно": 2, "удовлетворительно": 3, "хорошо": '4', "отлично": '5'}
a = {int(value): key for key, value in m.items() if 2 <= int(value) <= 5}
print(a)
# там, где цикл можно заменить на генератор, стоит это делать

# Задачи
print("\n", "Задачи", sep='')

# Task 2
# # Variant 1
# lst = input().split()
# d = {int(lst[0]) + i: x for i, x in enumerate(lst[1:])}
# print(d[4])
# # Variant 2
# n, *lst = input().split()
# d = {k: v for k, v in enumerate(lst, int(n))}
# print(d[4])

# Task 3
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# setN = set(lst_in)
# print(len(setN))

# Task 4
# set1 = {x.lower() for x in input().split() if len(x) > 2}
# print(len(set1))

# Task 5
# Variant 1 - мое решение, топ
# lst = input().lower().split()
# d = {x: lst.count(x) for x in set(lst)}
# print(d.get('и', 0))
# Variant 2 - замер времени
# from time import time
# beg = time()
# for i in range(10000):
#
#     lst = '''Как видно из примера, присвоение по новому ключу расширяет словарь,
#     присвоение по существующему ключу перезаписывает его, а попытка извлечения
#     несуществующего ключа порождает исключение. Для избежания исключения есть
#     специальный метод (см. ниже), или можно перехватывать исключение. Что же
#     можно еще делать со словарями? Да то же самое, что и с другими объектами:
#     встроенные функции, ключевые слова (например, циклы for и while), а также
#     специальные методы словарей. Как видно из примера, присвоение по новому ключу расширяет словарь,
#     присвоение по существующему ключу перезаписывает его, а попытка извлечения
#     несуществующего ключа порождает исключение. Для избежания исключения есть
#     специальный метод (см. ниже), или можно перехватывать исключение. Что же
#     можно еще делать со словарями? Да то же самое, что и с другими объектами:
#     встроенные функции, ключевые слова (например, циклы for и while), а также
#     специальные методы словарей.
#     '''.lower().split()
#     test = {x: lst.count(x) for x in lst}
# end = time()
# print(end - beg)
# beg1 = time()
# for x in range(10000):
#
#     lst = '''Как видно из примера, присвоение по новому ключу расширяет словарь,
#     присвоение по существующему ключу перезаписывает его, а попытка извлечения
#     несуществующего ключа порождает исключение. Для избежания исключения есть
#     специальный метод (см. ниже), или можно перехватывать исключение. Что же
#     можно еще делать со словарями? Да то же самое, что и с другими объектами:
#     встроенные функции, ключевые слова (например, циклы for и while), а также
#     специальные методы словарей. Как видно из примера, присвоение по новому ключу расширяет словарь,
#     присвоение по существующему ключу перезаписывает его, а попытка извлечения
#     несуществующего ключа порождает исключение. Для избежания исключения есть
#     специальный метод (см. ниже), или можно перехватывать исключение. Что же
#     можно еще делать со словарями? Да то же самое, что и с другими объектами:
#     встроенные функции, ключевые слова (например, циклы for и while), а также
#     специальные методы словарей.
#     '''.lower().split()
#     test = {x: lst.count(x) for x in set(lst)}
# end1 = time()
# print(end1 - beg1)

# Task 6
# # Variant 1 - четвертое место
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
from time import time

beg1 = time()
for i in range(100000):
    d = {}
    for x in lst_in:
        d.setdefault(x.split(': ')[0], set()).add(x.split(': ')[1])
end1 = time()
print(end1 - beg1)

# print(d)
# # Variant 2 - медленный, последнее место
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))

beg2 = time()
for i in range(100000):
    d = {}
    d = {i.split(':')[0]: {j.split(': ')[1] for j in lst_in if i.split()[0] == j.split()[0]} for i in lst_in}
end2 = time()
print(end2 - beg2)

# Variant 3 - третье место
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
beg3 = time()
for i in range(100000):
    lst = [i.split(": ") for i in lst_in]
    d = {}
    {d.setdefault(i[0], set()).add(i[1]) for i in lst}
end3 = time()
print(end3 - beg3)

# print(d)
# # Variant 4 - самый быстрый, 1-2 место
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
beg4 = time()
for i in range(100000):
    d = {}
    [d.setdefault(j[0], set()).add(j[1]) for j in [i.split(': ') for i in lst_in]]
end4 = time()
print(end4 - beg4)

# Variant 5 - медленный, предпоследнее место
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))

beg5 = time()
for i in range(100000):
    d = {}
    d = {author.split(': ')[0]: {book.split(': ')[1]
                                 for book in lst_in if book.split(': ')[0] == author.split(': ')[0]}
         for author in lst_in}
end5 = time()
print(end5 - beg5)

# # Variant 6 - самый быстрый, 1-2 место
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))

beg6 = time()
for i in range(100000):
    d = {}
    for c in [c.split(': ') for c in lst_in]:
        d.setdefault(c[0], set()).add(c[1])
end6 = time()
print(end6 - beg6)

# print(len(d))
