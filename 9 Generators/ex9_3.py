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

s = map(int, input().split())
a = list(s)
print(a)

# Task 1
# m = map(float, input().split())
#
# for i in range(3):
#     print(next(m), end=' ')
