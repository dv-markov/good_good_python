# 9.4 Функция filter

# filter(func, *iterables) - фильтрация элементов итерированного объекта

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = filter(lambda x: x % 2 == 0, a)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

b = filter(lambda x: x % 2 == 0, a)
print(*b)

b = filter(lambda x: x % 2 == 0, a)
for x1 in b:
    print(x1)

b = filter(lambda x: x % 2 == 0, a)
lst = list(b)
print(lst)

b = filter(lambda x: x % 2 == 0, a)
tp = tuple(b)
print(tp)


def is_prime(x):
    d = x -1
    if d < 0:
        return False

    while d > 1:
        if x % d == 0:
            return False
        d -= 1

    return True


def is_prime2(x):
    if x < 1:
        return False
    d = 2
    dmax = int(x ** 0.5)
    while d <= dmax:
        if x % d == 0:
            return False
        d += 1
    return True


b = filter(is_prime, a)
print(*b)

b = filter(is_prime2, a)
print(*b)

tp = ("Москва", "Рязань1", "Смоленск", "Тверь2", "Томск")

b = filter(str.isalpha, tp)
print(list(b))

# Nested filters
b1 = filter(is_prime2, a)
b2 = filter(lambda x: x % 2 != 0, b1)
print(*b2)

b2 = filter(lambda x: x % 2 != 0, filter(is_prime2, a))
print(*b2)


def is_prime3(x):
    if x < 1 or x % 2 == 0:
        return False
    d = 2
    dmax = int(x ** 0.5)
    while d <= dmax:
        if x % d == 0:
            return False
        d += 1
    return True


b = filter(is_prime3, a)
print(*b)

print("""
# Задачи
""")

# Task 1
# Variant 1
s = 'Тула Ульяновск Хабаровск Владивосток Омск Уфа'
cities = filter(lambda x: len(x) > 5, s.split())
# print(*cities)
for i in range(3):
    print(next(cities), end=' ')
print()
# Variant 2
cities = filter(lambda x: len(x) > 5, s.split())
print(*(next(cities) for _ in range(3)))


# Task 2
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# tp = tuple(map(lambda x: tuple(x.split('=')), lst_in))
# # print(tp)
# items_filtered = filter(lambda y: int(y[1]) > 500, tp)
# print(*(z[0] for z in items_filtered))


# Task 3
s = '8 11 0 -23 140 1'.split()
# s = input().split()
# print(s)
flt = filter(lambda x: 9 < abs(int(x)) < 100, s)
print(*flt)

# Task 4
# Variant 1
lst1 = '1 5 2 7 10 25 50 100'.split()
lst2 = '5 2 3 7 10 25 55'.split()
# lst1 = input().split()
# lst2 = input().split()
lst3 = filter(lambda x: x in lst2 and int(x) % 2 == 0, lst1)
print(*lst3)
# Variant 2
set1 = set('1 5 2 7 10 25 50 100'.split())
set2 = set('5 2 3 7 10 25 55'.split())
# set1 = set(input().split())
# set2 = set(input().split())
print(*sorted(filter(lambda x: int(x) % 2 == 0, set1 & set2)))

# Task 5

# Variant 1
from string import ascii_lowercase
chars = ascii_lowercase + "0123456789_@."

# emails = input().split()
emails = "abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com 654654sdfdsf 65454@jhjh@kjhkjh.ru ".split()
print(emails)
flt = filter(lambda x: x.count('@') == 1 and '.' in x.split('@')[1] and set(x) <= set(chars), emails)
print(*flt)

# Variant 2
from re import match

is_email = lambda email: match('\w+@\w+\.\w+', email)

print(*filter(is_email, emails))
