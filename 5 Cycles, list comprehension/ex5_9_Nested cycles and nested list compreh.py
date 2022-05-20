# 5.9 Вложенные циклы и вложенные генераторы списков

# вложенными являются циклы последующих уровней
print("\n", "Вложенные циклы", sep='')
a = [(i, j)
     for i in range(3)
     for j in range(4)
     ]
print(a)

# вложенные циклы с условиями
a = [(i, j)
     for i in range(3) if i % 3 == 0
     for j in range(4) if j % 2 == 0
     ]
print(a)

# таблица умножения
print("\n", "Таблица умножения", sep='')
a = [f'{i}*{j} = {i * j}'
     for i in range(3)
     for j in range(4)
     ]
print(a)

# распрямление списка
# во вложенных списках можно использовать переменные, объявленные в списках выше
print("\n", "Связь переменных во вложенных списках", sep='')
matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]
          ]
a = [x
     for row in matrix
     for x in row
     ]
print(a)

# в качестве оператора можно использовать еще один генератор списка
print("\n", "Генератор списка как оператор", sep='')
M, N = 3, 4
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(A)
AA = [[x ** 2 for x in row] for row in A]
print(AA)

a = [x ** 2
     for row in A
     for x in row
     ]
print(a)
# если из многомерного списка на выходе хотим получить многомерный, надо использовать вложенные генераторы
# если из многомерного хотим получить плоский, надо использовать вложенные циклы

# транспонирование с помощью вложенного генератора
print("\n", "Транспонирование с помощью вложенного генератора", sep='')
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(A)
A = [[row[i] for row in A] for i in range(len(A[0]))]
print(A)

# генератор списка в качестве итерируемого объекта
# используется для работы с вложенными функциями
print("\n", "Генератор списка в качестве итерируемого объекта", sep='')
g = [u ** 2 for u in [x + 1 for x in range(5)]]
print(g)

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# # Variant 1
# import sys
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# print(lst_in)
# # здесь продолжайте программу (используйте список lst_in)
# print(*[lst_in[i-1][j-1]
#         for i in range(len(lst_in), 0, -1)
#         for j in range(len(lst_in[0]), 0, -1)
#         ])
# # Variant 2
# import sys
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# lst = [j for i in lst_in[::-1] for j in i[::-1]]
# print(*lst)

# Task 2
# # Variant 1
# s = input().split()
# n = int(len(s) ** 0.5)
# lst = [[int(s[x]) for x in range(i, i + n)] for i in range(0, len(s), n)]
# print(lst)
# # Variant 2
# s = list(map(int, input().split()))
# n = int(len(s) ** 0.5)
# lst = [s[i:i+n] for i in range(0, len(s), n)]
# print(lst)

# Task 3
t = ["– Скажи-ка, дядя, ведь не даром",
     "Я Python выучил с каналом",
     "Балакирев что раздавал?",
     "Ведь были ж заданья боевые,",
     "Да, говорят, еще какие!",
     "Недаром помнит вся Россия",
     "Как мы рубили их тогда!"
     ]
lst = [[x for x in row.split() if len(x) > 3] for row in t]
print(lst)

# Task 4
# import sys
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# A = [[row[j] for row in lst_in] for j in range(len(lst_in[0]))]
# for row in A:
#     print(*row)
