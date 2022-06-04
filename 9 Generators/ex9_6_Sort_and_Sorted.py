# 9.6 Сортировка с помощью sort и sorted

a = [4, 3, -10, 1, 7, 12.5]
# метод sort ничего не возвращает
a.sort()
print(a)

b = [4, 3, -10, 1, 7, 12.5, "abc"]
# метод sort вернет ошибку
# a.sort()

a = [4, 3, -10, 1, 7, 12.5]
a.sort(reverse=True)
print(a)

# Функция sorted
a = [4, 3, -10, 1, 7, 12.5]
print(sorted(a))
print(sorted(a, reverse=True))

# Сортировка кортежей
r = ("Волга", "Лена", "Дон", "Енисей")
print(sorted(r))

# сортировка строки
print(sorted("python"))

# сортировка словарей
d = {"river": "река", "house": "дом", "tree": "дерево", "road": "дорога"}
# по умолчанию - сортировка ключей
print(sorted(d))
# сортировка значений
print(sorted(d.values()))
# сортировка пар ключ-значение
print(sorted(d.items()))
# сортировка словаря по ключам
print(dict(sorted(d.items())))

print("""
Задачи
""")

# Task 2
# s = input()
s = '-2 -1 8 11 4 5 '
lst = list(map(int, s.split()))
tp_lst = tuple(lst)
lst.sort()
tp_lst = tuple(sorted(tp_lst))
print(lst)
print(tp_lst)

# Task 3
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# Variant 1
def get_sort(d):
    return [v for k, v in sorted(d.items(), reverse=True)]
print(get_sort(d))
# Variant 2
def get_sort2 (d):
    return [d[i] for i in sorted(d, reverse=True)]
print(get_sort2(d))

# Task 4
# s = set(map(int, input().split()))
lst_in = '10 5 4 -3 2 0 5 10 3'
s = set(map(int, lst_in.split()))
print(*sorted(s, reverse=True)[:4])

# Task 5
# lst1 = map(int, input().split())
# lst2 = map(int, input().split())
lst1 = map(int, '7 6 4 2 6 7 9 10 4'.split())
lst2 = map(int, '-4 5 10 4 5 65'.split())
lst_sum = map(sum, zip(sorted(lst1), sorted(lst2, reverse=True)))
print(*lst_sum)


# Task 6
# Работа со словарями их сортировка
# dictionaries sorted

import sys
# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(lst_in)
lst_in = ['смартфон:120000',
          'яблоко:2',
          'сумка:560',
          'брюки:2500',
          'линейка:10',
          'бумага:500']


# Variant 1
def get3_least(d, l=3):
    return [v for k, v in sorted(d.items())[:l]]


d = dict(map(lambda x: x.split(':')[::-1], lst_in))
d = {int(k): v for k, v in d.items()}
print(*get3_least(d))

# Variant 2
def get_cheap(d):
    return list(dict(sorted(d.items())[:3]).values())
dct = {int(b) : a for a, b in [x.split(':') for x in lst_in]}
print(*get_cheap(dct))

# Variant 3 - Glozmann
def best3(d):
    return [d[key] for key in sorted(d)[:3]]
d = {}
for s in lst_in:
    item, price = s.split(':')
    d[int(price)] = item
print(*best3(d))

# Variant 4 - my upgrade
def get_least(d, l=3):
    return [d[key] for key in sorted(d)[:l]]


# d = dict(map(lambda x: x.split(':'), lst_in))
d = {int(k): v for v, k in map(lambda x: x.split(':'), lst_in)}
print(*get_least(d))
