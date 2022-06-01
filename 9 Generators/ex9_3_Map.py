# 9.3 Функция map

b = map(int, ['1', '2', '3', '5', '7'])
for x in b:
    print(x, end=" ")
print()

b = map(int, ['1', '2', '3', '5', '7'])
a = list(b)
print(a)

# map - это генератор (итератор), в котором заданная функция применяется последовательно
# к элементам последовательности
b = (int(x) for x in ['1', '2', '3', '5', '7'])
a = list(b)
print(a)

b = map(int, ['1', '2', '3', '5', '7'])
a = sum(b)
print(a)

# Дважды пройтись по коллекции map нельзя
b = map(int, ['1', '2', '3', '5', '7'])
a = max(b)
print(a)

cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]
b = map(len, cities)
a = list(b)
print(a)

# вызов метода
b = map(str.upper, cities)
a = list(b)
print(a)


# задание и вызов функции как метода
def symbols(s):
    return list(s.lower())


b = map(symbols, cities)
a = list(b)
print(a)

# использование lambda функции
b = map(lambda s: list(s.lower()), cities)
a = list(b)
print(a)

b = map(lambda s: s[::-1], cities)
a = list(b)
print(a)

# s = map(int, input().split())
# a = list(s)
# print(a)

# Task 1
# m = map(float, input().split())
#
# for i in range(3):
#     print(next(m), end=' ')

# Task 2
# lst = list(map(lambda x: abs(int(x)), input().split()))
# print(*lst)

# Task 3
# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# # переменную lst_in не менять!
# print(lst_in)
# lst2D = [list(map(int, x.split())) for x in lst_in]
# print(lst2D)

# Task 4
# ввод строки (переменную s не менять)
# s = input()
s = 'house=дом car=машина men=человек tree=дерево'
s_lst = s.split()
# здесь продолжайте программу
print(s_lst)
[print(x) for x in s_lst]
tp = tuple(tuple(x.split('=')) for x in s_lst)
print(tp)

# Variant 2
# s = input()
s_lst = s.split()
tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
print(tp)

# Task 5
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# s = input()
s = 'Привет Питон'
res = map(lambda x: t.get(x, '-'), s.lower())
print(''.join(res))

# Task 6
s = 'Москва Уфа Вологда Тула Владивосток Хабаровск'
# s = input()
lst = map(lambda x: x if len(x) > 5 else '-', s.split())
print(*lst)
