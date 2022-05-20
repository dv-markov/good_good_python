# 7.5 Функции с произвольным числом параметров
# *args и **kwargs

from time import time

m = max(1, 2, 3, 4, -5)
print(m)


def os_path(*args, sep='\\'):
    # print(args)
    # При указании *args функция принимает кортеж из аргументов
    # * - оператор упаковки аргумента
    path = sep.join(args)
    return path


p = os_path("F:\\~stepik.org", "Добрый, добрый Python", "39\\p39. Functions.docx")
print(p)

p = os_path()
print(p)

# Формальные параметры можно указывать при вызове функции как именованные аргументы,
# только если они были явно указаны при объявлении функции
p = os_path("F:\\~stepik.org",
            "Добрый, добрый Python",
            "39\\p39. Functions.docx",
            sep='/')
print(p)


# произвольное количество именованных аргументов реализовать следующим образом
def os_path1(*args, **kwargs):
    # при указании kwargs функция принимает словарь из именованных аргументов
    # print(kwargs)
    path = kwargs['sep'].join(args)
    return path


# при этом аргументы, используемые в теле функции, обязательно надо указывать при ее вызове
p = os_path1("F:\\~stepik.org",
             "Добрый, добрый Python",
             "39\\p39. Functions.docx",
             sep='/', trim=True)
print(p)


# комбинация именованных и произвольных формальных параметров
# формальные именованные параметры должны идти до соответствующей коллекции
def os_path2(*args, sep='\\', **kwargs):
    path = sep.join(args)
    return path


p = os_path2("F:\\~stepik.org",
             "Добрый, добрый Python",
             "39\\p39. Functions.docx",
             sep='/', trim=True)
print(p)


# аналогично с очередностью указания фактических параметров и коллекций
def os_path3(disk, *args, sep='\\', **kwargs):
    args = (disk, ) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]
    path = sep.join(args)
    return path


p = os_path3("F:", "~stepik.org   ",
             "  Добрый, добрый Python",
             "  39\\p39. Functions.docx",
             sep='/', trim=True)
print(p)

p = os_path3("F:", "~stepik.org   ",
             "  Добрый, добрый Python",
             "  39\\p39. Functions.docx",
             sep='/', trim=False)
print(p)

p = os_path3("F:", "~stepik.org   ",
             "  Добрый, добрый Python",
             "  39\\p39. Functions.docx",
             sep='/')
print(p)

# Задачи
print("\n", "Задачи", sep='')


# Task 3
# def get_even(*args):
#     return [x for x in args if not x % 2]
#
#
# lst = list(map(int, input().split()))
# print(lst)
# print(*lst)
# # в *args можно передавать список чисел, при этом он должен быть распакован
# print(get_even(*lst))


# Task 4
# # Variant 1 - мой
# def get_biggest_city(*args):
#     d = {}
#     [d.setdefault(x, len(x)) for x in args]
#     return list(d.keys())[list(d.values()).index(max(d.values()))]
#
#
# # Variant 2 - мой
# # почти в три раза быстрее первого варианта
# def get_biggest_city2(*args):
#     biggest_city = args[0]
#     for x in args[1:]:
#         if len(x) > len(biggest_city):
#             biggest_city = x
#     return biggest_city
#
#
# # Variant 3 - самый быстрый, используется функция макс. по значению длины строки
# # Функцию max, как и sort, можно вызывать с ключом - методом, который будет применяться к каждому элементу сравнения
# def get_biggest_city3(*args):
#     return max(args, key=len)
#
#
# # Variant 4
# def get_biggest_city4(*args):
#     s = {len(i):i for i in args}
#     return s[max(s)]
#
# lst = input().split()
#
# ts1 = time()
# for i in range(1000000):
#     a = get_biggest_city(*lst)
# te1 = time()
# print(get_biggest_city(*lst))
# print('F1, t =', te1 - ts1)
#
# ts2 = time()
# for i in range(1000000):
#     a = get_biggest_city2(*lst)
# te2 = time()
# print(get_biggest_city2(*lst))
# print('F2, t =', te2 - ts2)
#
#
# ts3 = time()
# for i in range(1000000):
#     a = get_biggest_city3(*lst)
# te3 = time()
# print(get_biggest_city3(*lst))
# print('F3, t =', te3 - ts3)


# Task 5
# def get_data_fig(*args, **kwargs):
#     arg_seq = ('type', 'color', 'closed', 'width')
#     res = [sum(args)] + [kwargs.get(x) for x in arg_seq if x in kwargs]
#     return tuple(res)
#
# why not?
# def get_data_fig1(*args, **kwargs):
#     arg_seq = ('type', 'color', 'closed', 'width')
#     return sum(args), *[kwargs.get(x) for x in arg_seq if x in kwargs]
#
#
# print(get_data_fig(4, 5, 1))
# print(get_data_fig(4, 5, 1, type=True, color=654, closed=False, width=5))
# print(get_data_fig(4, 5, 1, width=500, type=False, color=456, closed=False))

# Task 6

# проверка элемента матрицы на изолированность (поиск 1 вокруг 1)

# # Variant 0 - на втором месте по скорости, решение из топ-1
# def is_isolate0(*args):
#     return sum(*args) < 2
#
#
# def verify0(lst):
#     size = len(lst)
#     return False not in [is_isolate0(lst[i][j:j+2] + lst[i+1][j:j+2])
#                          for j in range(size - 1)
#                          for i in range(size - 1)]
#
#
# # Variant 1 - мой, самый быстрый
# def verify(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(n):
#             if lst[i][j] == 1:
#                 di_up = 0 if i == 0 else 1
#                 di_down = 1 if i == n else 2
#                 dj_left = 0 if j == 0 else 1
#                 dj_right = 1 if j == n else 2
#                 # print([x
#                 #        for row in lst[i-di_up:i+di_down]
#                 #        for x in row[j-dj_left:j+dj_right]])
#                 if not is_isolate(*[x
#                                     for row in lst[i-di_up:i+di_down]
#                                     for x in row[j-dj_left:j+dj_right]]
#                                   ):
#                     return False
#     else:
#         return True
#
#
# def is_isolate(*args):
#     return True if sum(args) == 1 else False
#
#
# # Variant 2 - мой альтернативный, без учета граничных значений
# # def verify(lst):
# #     for i in range(1, len(lst) - 1):
# #         for j in range(1, len(lst[0]) - 1):
# #             if lst[i][j] == 1:
# #                 print([row[j-1:j+2] for row in lst[i-1:i+2]])
# #                 if not is_isolate([row[j-1:j+2] for row in lst[i-1:i+2]]):
# #                     return False
# #     else:
# #         return True
# #
# #
# # def is_isolate(surround):
# #     return True if sum([x for row in surround for x in row]) == 1 else False
#
#
# # Variant 3 - Glozmann, крайне медленный
# def is_not_isolate3(i, j, m):
#     return m[i][j] and any((m[i][j - 1], m[i][j + 1], m[i + 1][j], m[i + 1][j + 1]))
#
#
# def verify3(m):
#     for row in m: row.append(0)
#     m.append([0] * len(m[0]))
#
#     return not any(is_not_isolate3(i, j, m)
#                    for i in range(len(m) - 1)
#                    for j in range(len(m[0]) - 1))
#
#
# # Variant 4 - алгоритмический, на втором месте по скорости, не по заданию. Andrii Sabo
# def verify4(s):
#     for i in range(len(s) - 1):
#         ls = [s[i][j] + s[i + 1][j] for j in range(len(s))]
#         if '11' in ''.join([str(x) for x in ls]) or 2 in ls:
#             return False
#     return True
#
#
# import sys
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# # print(verify(lst_in))
#
# # Проверка скорости работы алгоритма
# ts0 = time()
# for k in range(100000):
#     a = verify0(lst_in)
# te0 = time()
# print(verify0(lst_in))
# print('F0, t =', te0 - ts0)
#
# ts1 = time()
# for k in range(100000):
#     a = verify(lst_in)
# te1 = time()
# print(verify(lst_in))
# print('F1, t =', te1 - ts1)
#
# ts4 = time()
# for k in range(100000):
#     a = verify4(lst_in)
# te4 = time()
# print(verify4(lst_in))
# print('F4, t =', te4 - ts4)


# print([x[0:3] for x in lst_in[1:2]])
# print(*[x for row in lst_in[0:3] for x in row[0:3]])
# print(is_isolate(lst_in[0][0+1], *lst_in[0+1][0:0+2]))
# print(is_isolate(*list(map(int, input().split()))))

# 1 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# True
#
# 0 1 0 0 1
# 1 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 1
# 1 0 0 1 0
# False
#
# 0 1 0 0 1
# 1 0 0 1 0
# 0 0 1 0 0
# 0 1 0 0 1
# 1 0 0 1 0
# False
#
# 1 0 1 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# False
#
# 1 0 0 0 0 1 0 0 0 0
# 0 0 1 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 1 0 1 0 0 1 0 1 0
# 0 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 1 0 0 0 0
# 0 0 1 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 1 0 1 0 0 1 0 1 0
# 0 0 0 0 0 0 0 0 0 0
# True

# Task 7
# def str_min(s1, s2):
#     return s1 if s1 < s2 else s2
#
#
# def str_min3(s1, s2, s3):
#     return str_min(str_min(s1, s2), s3)
#
#
# def str_min4(s1, s2, s3, s4):
#     return str_min(str_min3(s1, s2, s3), s4)
#
#
# # работает медленнее, чем простое сравнение
# def str_min2(s1, s2):
#     return min(s1, s2)
#
#
# str1, str2 = input(), input()
#
# # Проверка скорости работы алгоритмов
# ts1 = time()
# for k in range(10000000):
#     a = str_min(str1, str2)
# te1 = time()
# print(str_min(str1, str2))
# print('F1, t =', te1 - ts1)
#
# ts2 = time()
# for k in range(10000000):
#     a = str_min2(str1, str2)
# te2 = time()
# print(str_min2(str1, str2))
# print('F2, t =', te2 - ts2)


