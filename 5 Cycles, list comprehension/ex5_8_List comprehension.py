# 5.8 Генераторы списков (List comprehension)

N = 6

# Решение со стандартным циклом for
a = [0] * N
for i in range(N):
    a[i] = i ** 2
print(a)

# генератор списков - работает быстрее, чем обычный цикл for
a = [x ** 2 for x in range(N)]
print(a)

b = [1 for x in range(5)]
print(b)

N = 7
b = [1 for x in range(N)]
print(b)
# переменная x доступна только внутри генератора

c = [1] * N
print(c)

a = [x % 4 for x in range(N)]
print(a)

a = [x % 2 == 0 for x in range(N)]
print(a)

a = [0.5 * x + 1 for x in range(N)]
print(a)

# В качестве способа формирования значения генератора списков можно записывать любые конструкции языка Python
# работает быстрее, чем циклы while и for

# d_inp = input("Целые числа через пробел: ")
# print(d_inp.split())
# a = [int(d) for d in d_inp.split()]
# print(a)

a = [d for d in "python"]
print(a)
a = [ord(d) for d in "python"]
print(a)

# генератор от списка строк возвращает список строк
ts = 'Я б Python выучил только за то что есть он на этом канале'
t = ts.split()
print(t)
a = [d for d in t]
print(a)
b = [len(d) for d in t]
print(b)

# генераторы списков с условием
a = [x for x in range(-5, 5) if x < 0]
print(a)

a = [x for x in range(-5, 5) if x % 2 == 0]
print(a)

a = [x for x in range(-6, 7) if x % 2 == 0 and x % 3 == 0]
print(a)

cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]
a = [city for city in cities if len(city) < 7]
print(a)

# тернарный условный оператор для генератора списка
d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
print(d)

a = ["четное" if x % 2 == 0 else "нечетное" for x in d]
print(a)

a = ["четное" if x % 2 == 0 else "нечетное"
     for x in d
     if x > 0
     ]
print(a)

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# a = input().split()
# lst = [abs(float(x)) for x in a]
# print(*lst)

# Task 2
# lst = [int(x) for x in input()]
# print(lst)

# Task 3
# Подвиг 3. Вводится натуральное число N.
# С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы.
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла).
# Результат вывести в виде таблицы чисел как показано в примере ниже.
# N = int(input())
# lst = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
# for r in lst:
#     print(*r)


# Task 4
# Variant 1
# c = input().split()
# lst = [x for x in c if len(x) > 5]
# print(*lst)
# Variant 2
# print(*[x for x in input().split() if len(x) > 5])

# Task 5
# n = int(input())
# print(*[x for x in range(1, n + 1) if n % x == 0])

# Task 6
# n = int(input())
# lst = [[x] * n for x in range(n)]
# for r in lst:
#     print(*r)

# Task 7
# print(*[x for i, x in enumerate(input().split()) if i % 2 == 0])

# Task 8
# lst1, lst2 = input().split(), input().split()
# print(*[int(lst1[i]) + int(lst2[i]) for i in range(len(lst1))])

# Task 9
# s = input().split()
# lst = [[s[i], int(s[i+1])] for i in range(0, len(s), 2)]
# print(lst)

