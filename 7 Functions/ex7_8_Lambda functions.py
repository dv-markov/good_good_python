# 7.8 Анонимные (lambda) функции

s = lambda a, b: a + b
s(1, 2)
print(s(1, 2))

# lambda функция может быть записана как элемент любой конструкции языка Python
a = [4, 5, lambda: print("lambda"), 7, 8]
print(a)
a[2]()

# обычно lambda функция выполняет определенное действие и возвращает результат
lst = [5, 3, 0, -6, 8, 10, 1]


def get_filter(a, filter=None):
    if filter is None:
        return a

    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res


r = get_filter(lst)
print(r)

r = get_filter(lst, lambda x: x % 2 == 0)
print(r)

r = get_filter(lst, lambda x: x > 0)
print(r)

# Внутри лямбда-функции можно прописать только одну определенную конструкцию языка Python (одну команду)
# Lambda-функции нельзя писать в несколько строчек
# Также нельзя использовать оператор присваивания

print(lambda a: a + 1)


# Задачи
print("\n", "Задачи", sep='')


# Task 2
get_sq = lambda x: x**2
print(get_sq(5))

# Task 3
get_div = lambda a, b: None if b == 0 else a / b
print(get_div(10, 2))

# Task 4
# Variant 1
# x = float(input())
# absolute = lambda x: -x if x < 0 else x
# print(absolute(x))
# Variant 2
# print((lambda x: -x if x < 0 else x)(float(input())))

# Task 5
# s = input()
# print((lambda b: 'ra' in b)(s))


# Task 6

# # Variant 1
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


# здесь продолжайте программу
lst_in = list(map(int, input().split()))  # 5 4 -3 4 5 -24 -6 9 0

print(filter_lst(lst_in))
print(filter_lst(lst_in, lambda x: x < 0))
print(filter_lst(lst_in, lambda x: x >= 0))
print(filter_lst(lst_in, lambda x: 3 <= x <= 5))

# # Variant 2
# изменил начальную функцию, использовал фильтр-функцию
# минус - функция печатает, а не возвращает значения
# приоритетный вариант - 1 или 3
# it = list(map(int, input().split()))
#
#
# def filter_lst(it, key=None):
#     if key is None:
#         print(*it)
#     else:
#         print(*it)
#         for i in key:
#             print(*filter(i, it))
#
#
# filter_lst(it, key=[lambda x: x < 0, lambda x: x >= 0, lambda x: 3 <= x <= 5])


# # Variant 3
# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
#
# # здесь продолжайте программу
# lst = list(map(int, input().split()))
# lambda_list = [None, lambda x: x < 0, lambda x: x >= 0, lambda x: 3 <= x <= 5]
# for l in lambda_list:
#     print(*filter_lst(lst, l))

