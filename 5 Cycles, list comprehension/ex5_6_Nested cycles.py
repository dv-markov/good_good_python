# 5.6 Вложенные циклы

# матрица
for i in range(1, 4):
    for j in range(1, 6):
        print(f"i = {i}, j = {j};", end=' ')
    print()
print()

# перебор двумерного списка
a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
for row in a:
    # print(row, type(row))
    for x in row:
        print(x, type(x), end=' ')
    print()
print()

# сложение двух списков
b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
c = []
for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])
    c.append(r)
print(c)
print()

# удаление пробелов в списке строк
t = ["- Скажи-ка, дядя, ведь не даром",
     "Я Python выучил с  каналом",
     "Балакирев что   раздавал?",
     " Ведь были   ж заданья боевые,",
     "Да, говорят,  еще какие!",
     "Недаром помнит    вся Россия",
     "Как мы рубили    их тогда!"
     ]
for i, line in enumerate(t):
    while line.count('  '):
        line = line.replace('  ', ' ')
    t[i] = line
print(t)
print()

# M, N = list(map(int, input("Введите M и N: ").split()))
# zeros = []
# for i in range(M):
#     zeros.append([0] * N)
# print(zeros)
#
# for i in range(M):
#     for j in range(N):
#         zeros[i][j] = 1
# print(zeros)

# транспонирование матрицы
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]
for r in A:
    for x in r:
        print(x, end='\t')
    print()

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# N = int(input())
# for i in range(N):
#     for j in range(N-1):
#         print(1, end=' ')
#     print(5)

# Task 2
# # Variant 1
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# for r in lst_in:
#     while r.count('  '):
#         r = r.replace('  ', ' ')
#     r = r.replace(' ', '-')
#     print(r)
# Variant 2
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# for i in lst_in:
#     print('-'.join(i.split()))

# Task 3
# все простые числа до n
# # Variant 1
# n = int(input())
# for x in range(2, n):
#     flg = True
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             flg = False
#     print(['', str(x) + ' '][flg], end='')
# Variant 2
# n = int(input())
# for i in range(2, n):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

# Task 4

# Variant 1
# import sys
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# # print(lst_in)
# lst = [[0] * len(lst_in[0]), *lst_in, [0] * len(lst_in[0])]
# # print(lst)
# for i, r in enumerate(lst):
#     lst[i] = [0] + r + [0]
# # print(lst)
# flg = 'ДА'
# for i in range(1, len(lst)):
#     for j in range(1, len(lst[i])):
#         if lst[i][j] == 1:
#             if sum(lst[i - 1][j - 1:j + 2]) + sum(lst[i][j - 1:j + 2]) + sum(lst[i + 1][j - 1:j + 2]) > 1:
#                 flg = 'НЕТ'
#                 break
#     if flg == 'НЕТ':
#         break
# print(flg)

# # Variant 2
# import sys
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# # здесь продолжайте программу (используйте список lst_in)
# n = len(lst_in) - 1
# for i in range(n):
#     for j in range(n):
#         if lst_in[i][j] + lst_in[i + 1][j] + lst_in[i + 1][j + 1] + lst_in[i][j + 1] > 1:
#             print('НЕТ')
#             break
#     else:
#         continue
#     break # выход из внешнего цикца
# else:
#     print('ДА')

# Variant 3
import sys
# n, ans = 5, 'ДА'
# s = sys.stdin.readlines()
# mtx = [list(map(int, x.strip().split())) + [0] for x in s] + [[0] * (n + 1)]
# for i in range(n):
#     for j in range(n):
#         if mtx[i][j] == 1 and any((mtx[i][j + 1], mtx[i + 1][j], mtx[i + 1][j + 1])):
#             ans, i, j = 'НЕТ', n, n
# print(ans)


# Task 5
# # Variant 1
# import sys
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# s_row = [0]*len(lst_in)
# s_col = [0]*len(lst_in[0])
# for i, r in enumerate(lst_in):
#     s_row[i] = sum(r)
#     for j, c in enumerate(r):
#         s_col[j] += c
# print(['НЕТ', 'ДА'][s_row == s_col])
# # Variant 2
# import sys
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# flag = 'ДА'
# for i in range(5):
#     for j in range(5):
#         if lst_in[i][j] != lst_in[j][i]:
#             flag = 'НЕТ'
# print(flag)
# # Variant 3 - обход нижнего треугольника
# import sys
# lst_in = [list(map(int, x.strip().split())) for x in sys.stdin]
# print(('НЕТ', 'ДА')[all(lst_in[i][j] == lst_in[j][i] for i in range(len(lst_in)) for j in range(i))])

# Task 6 - сортировка методом выбора
# lst = list(map(int, input().split()))
# for i in range(len(lst)-1):
#     min_el = lst[i]
#     k = i
#     for j in range(i+1, len(lst)):
#         if lst[j] < min_el:
#             k = j
#             min_el = lst[j]
#     lst[i], lst[k] = min_el, lst[i]
# print(*lst)

# Task 6 - сортировка методом пузырька
# # Variant 1
# lst = list(map(int, input().split()))
# for i in range(len(lst), 1, -1):
#     for j in range(1, i):
#         if lst[j] < lst[j - 1]:
#             lst[j], lst[j - 1] = lst[j - 1], lst[j]
# print(*lst)
# # Variant 2
# lst = list(map(int, input().split()))
# for i in range(len(lst)-1, 0, -1):
#     for j in range(i):
#         if lst[j + 1] < lst[j]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
# print(*lst)

# Task 7
# n = int(input())
# d = 64
# while n > 0:
#     if n >= d:
#         print(d, end=' ')
#         n -= d
#     else:
#         d = d // 2

