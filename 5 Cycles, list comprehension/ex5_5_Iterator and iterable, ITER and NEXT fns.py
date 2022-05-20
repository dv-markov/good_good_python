# 5.5 Итератор и итерируемые объекты. Функции iter и next

d = [5, 3, 7, 10, 32]
print(d)
print(iter(d))
it = iter(d)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# по окончании функция next возвращает ошибку StopIteration
# можно задать второй аргумент для функции next, который она будет возвращать по окончании итерируемого объекта

s = "python"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

r = range(5)
it = iter(r)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# цикл for перебирает элементы коллекции за счет применения итератора

# Задачи
print("\n", "Задачи", sep='')

# Task 3
# it = iter(input())
# x = ''
# while x != ' ':
#     x = next(it)
#     print(x, end='')

# Task 4
# Variant 1
# s = input()
# it = iter(s)
# for x in s:
#     print(next(it), end=' ')
# # Variant 2
# Если передать в функцию next второй аргумент, то он вернётся вместо ошибки
# it = iter(input())
# i = next(it, '.')
# while i != '.':
#     print(i, end=' ')
#     i = next(it, '.')
#
