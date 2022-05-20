# 7.7 Рекурсивные функции
from time import time


def recursive(value):
    print(value)
    if value < 4:
        recursive(value + 1)
    print(value)


# стек вызова рекурсивной функции (maximum recursion depth) в Python = 997
# функции добавляются в стек, затем извлекаются обратно в порядке LIFO
recursive(1)


def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)


p = fact(6)
print(p)

p = fact(7)
print(p)

# Обход файловой системы через рекурсию
F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['Readme.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bar', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):
    for f in path:
        print(" "*depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth+1)
        else:
            print(" "*(depth+1), " ".join(path[f]))


get_files(F)


# Задачи
print("\n", "Задачи", sep='')


# Task 2
# Список чисел от 1 до n
def get_rec_N(N):
    if N > 1:
        get_rec_N(N-1)
    print(N)


n = 8
get_rec_N(n)


# Task 3
# Сумма списка через рекурсию
# Variant 1 - мой, самый быстрый. Скорость алгоритма выше на 30-40%
# def get_rec_sum(lst, ind=0):
#     if ind < len(lst) - 1:
#         # print(lst, id(lst))
#         return lst[ind] + get_rec_sum(lst, ind + 1)
#     else:
#         return lst[ind]
# #
#
# lst_in = list(map(int, input().split()))
# print(get_rec_sum(lst_in))
#
# # Variant 2 - Timohin - третье место
# lst1 = [int(i) for i in input().split()]
#
# def get_rec_sum2(lst):
#     head, *tail = lst
#     # print(lst, id(lst))
#     return head + get_rec_sum2(tail) if tail else head
#
# print(get_rec_sum(lst1))
#
# # Variant 3 - Anonymous 162398320 - второе место
# n = list(map(int, input().split()))
#
# def get_rec_sum3(n):
#    # print(n, id(n))
#     return 0 if len(n) == 0 else get_rec_sum3(n[1:]) + n[0]
#
# print(get_rec_sum(n))


# Variant 4 - тест с распаковкой, самый долгий
# def get_rec_sum4(*lst):
#     return lst[0] + get_rec_sum4(*lst[1:]) if len(lst) else 0
    # if ind < len(lst) - 1:
    #     return lst[ind] + get_rec_sum(lst, ind + 1)
    # else:
    #     return lst[ind]


# time test
# lst_in = list(map(int, input().split()))
#
# ts1 = time()
# for k in range(1000000):
#     a = get_rec_sum(lst_in)
# te1 = time()
# print(get_rec_sum(lst_in))
# print('F1, t =', te1 - ts1)
#
# ts2 = time()
# for k in range(1000000):
#     a = get_rec_sum2(lst_in)
# te2 = time()
# print(get_rec_sum2(lst_in))
# print('F2, t =', te2 - ts2)
#
# ts3 = time()
# for k in range(1000000):
#     a = get_rec_sum3(lst_in)
# te3 = time()
# print(get_rec_sum3(lst_in))
# print('F3, t =', te3 - ts3)

# # вызов функций подряд с печатью адресов
# print(get_rec_sum(lst_in))
# print(get_rec_sum2(lst_in))
# print(get_rec_sum3(lst_in))


# Task 4
# Числа Фибоначчи
# Variant 1 - мой вариант, учитывает любые варианты входных данных
def fib_rec(N, f=[]):
    if len(f) < 1:
        return fib_rec(N, [1, 1])
    elif len(f) < N:
        return fib_rec(N, f + [sum(f[-2:])])
    else:
        return f[:N]


# # Variant 2 - без использования аргумента f
# def fib_rec1(N, f=[]):
#     if N < 3:
#         return [1] * N
#     lst = fib_rec(N-1)
#     lst.append(lst[-1] + lst[-2])
#     return lst
#
print(fib_rec(10))
print(fib_rec(4, [1, 1, 2, 3, 5, 8, 13]))
print(fib_rec(8, [1, 1, 2, 3, 5, 8, 13]))
print(fib_rec(15, [1, 1, 2, 3]))


# Task 5
# Факториал
def fact_rec(n):
    if n < 2:
        return 1
    else:
        return n * fact_rec(n-1)


print(fact_rec(6))


# Task 6
# Преобразование многомерного списка в одномерный
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


# # Variant 1 - мой 1
# def get_line_list(d, a=[]):
#     for x in d:
#         if type(x) == list:
#             get_line_list(x, a)
#         else:
#             a.append(x)
#     return a


# Variant 2 - мой 2, с проверкой а
def get_line_list(d, a=None):
    if a is None:
        a = []
    for x in d:
        # можно также использовать функцию issubstance
        if type(x) == list:
            get_line_list(x, a)
        else:
            a.append(x)
    return a


print(get_line_list(d))
print(get_line_list(d))


# Task 7
# Лягушка Фибоначчи
# Variant 1
def get_path(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    else:
        return get_path(n-1) + get_path(n-2)

# Variant 2
# def get_path1(n):
#     return n if n in (1, 2) else get_path(n - 1) + get_path(n - 2)


# a = int(input())
a = 7
print(get_path(a))


# Task 8 - lecture
# Метод слияния списков
# С использованием рекурсии
# Слияние списков
# Сортировка массива методом слияния
# Вычислительная сложность N*log(2)N = 7 * log(2)7 < 21
# Простейшие алгоритмы имеют сложность O(N^2) = 7^2 = 49
# Великий подвиг 8

# def div_lst(lst):
#     if len(lst) > 1:
#         dl = round(len(lst)/2)
#         return lst[:dl], lst[dl:]

def merge_lst(l1, l2):
    lst = []
    i = j = 0
    while i < len(l1):
        while j < len(l2) and l2[j] < l1[i]:
            lst.append(l2[j])
            j += 1
        lst.append(l1[i])
        i += 1
    if j < len(l2):
        lst += l2[j:]
    return lst


def sort_mrg(lst):
    if len(lst) > 1:
        dl = round(len(lst)/2)
        return merge_lst(sort_mrg(lst[:dl]), sort_mrg(lst[dl:]))
    else:
        return lst


lst_in = list(map(int, input().split()))
print(*sort_mrg(lst_in))

# lst1 = [1, 4, 6, 8]
# lst2 = [2, 5, 7, 15]
# lst3 = [7, 4, 2, 0, 5]
# lst4 = [1, 3]
# lst5 = [1, 3, 5]
# lst6 = [1, 4, 10, 11]
# lst7 = [2, 3, 3, 4, 8]
# lst8 = [8, 11, -6, 3, 0, 1, 1]

# Variant 2
# l = [int(i) for i in input().split()]
# def merge_two_lists(a, b):
#     res = []
#     while a and b:
#         res += [a.pop(0) if a[0] < b[0] else b.pop(0)]
#     return res + a + b
# def merge_sort(l):
#     if len(l) == 1:
#         return l
#     mid = len(l) // 2
#     a, b = l[:mid], l[mid:]
#     return merge_two_lists(merge_sort(a), merge_sort(b))
# print(*merge_sort(l))
