# 5.3 Оператор цикла for и функция range

# цикл for применяется для итерируемых объектов
d = [1, 2, 3, 4, 5]
for x in d:
    print(x)

for x in "python":
    print(x)

# при изменении переменной цикла элементы объекта не меняются
for x in d:
    x = 0
print(d)

p = 1
for x in d:
    p *= x
print(p)

# для изменения элементов списка к ним нужно обращаться по индексу
for i in [0, 1, 2, 3, 4]:
    d[i] = 0
print(d)

# функция range
# range(start, stop, step)
# range(start, stop)
# range(stop)
# последнее значение не входит в сгенерированные значения
print(range(5))
print(list(range(5)))
print(list(range(2)))
print(list(range(0)))
print(list(range(-5)))
print(list(range(0, -5)))
print(list(range(-10, -5)))
print(list(range(-10, -5, 2)))
print(list(range(-10, -5, -2)))
print(list(range(-10, -20, -2)))
print(list(range(5, 0, -1)))
print(list(range(5, -1, -1)))

for i in range(5):
    d[i] = 0
print(d)

for i in range(len(d)):
    d[i] = 0
print(d)

# S = 1/2 + 1/3 + 1/4 + 1/10 + ... + 1/1000
S = 0
for i in range(2, 1001):
    S += 1/i
print(S)

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# # Variant 1
# rng = list(range(11))
# print(*rng)
# Variant 2
print(*range(11))

# Task 2
print(*range(10, -1, -1))

# Task 5
# интересные альтернативные решения с циклом for-условием, умножением на True и тернарным оператором
# # Variant 1
# lst = list(map(int, input().split()))
# s = 0
# for x in lst:
#     if x % 2 != 0:
#         s += x
# print(s)
# # Variant 2
# print(sum([i for i in map(int, input().split()) if i % 2 != 0]))
# # Variant 3
# print(sum((e % 2) * e for e in map(int, input().split())))
# # Variant 4
# s = 0
# for i in map(int, input().split()):
#     s += i if i % 2 else 0
# print(s)

# Task 6
# # Variant 1
# cities = input().split()
# for i in range(len(cities)):
#     cities[i] = len(cities[i])
# print(*cities)
# # Variant 2
# print(*map(len, input().split()))

# Task 7
# # Variant 1 - O(n)
# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)
# # Variant 2 - O(n/2)
# n = int(input())
# for d in range(1, n // 2 + 1):
#     if n % d == 0:
#         print(d)
# print(n)
# # Variant 3 - O(sqrt(n))
# from collections import deque
# n = int(input())
# nsqrt = n ** .5
# factors = deque()
# if nsqrt.is_integer():
#     factors.append(int(nsqrt))
# for i in range(int(nsqrt) - nsqrt.is_integer(), 0, -1):
#     if n % i == 0:
#         factors.appendleft(i)
#         factors.append(n // i)
# print(*factors, sep='\n')

# Task 8
# # Variant 1
# n = int(input())
# flag = 'ДА'
# for i in range(2, int(n/2)):
#     if n % i == 0:
#         flag = 'НЕТ'
#         break
# print(flag)
# # Variant 2
# n = int(input())
# print(('НЕТ', 'ДА')[n > 1 and all(n % i for i in range(2, int(n **.5) + 1))])

# Task 9
# cities = input().lower().split()
# ign_letters = ['ь', 'ъ', 'ы']
# flag = 'ДА'
# for i in range(0, len(cities) - 1):
#     if (cities[i][-2] if cities[i][-1] in ign_letters else cities[i][-1]) != cities[i+1][0]:
#         flag = 'НЕТ'
#         break
# print(flag)

# Task 10
# # Variant 1
# n = int(input())
# s = 0
# for i in range(3, n):
#     if i % 3 == 0 or i % 5 == 0:
#         s += i
# print(s)
# # Variant 2
# print(sum([x for x in range(1, n) if x % 3 == 0 or x % 5 == 0]))
