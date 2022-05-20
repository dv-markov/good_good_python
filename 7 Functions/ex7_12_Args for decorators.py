# 7.12 Передача аргументов декораторам
# Декораторы функций с параметрами
import math


# Декорирование через @ с параметром
def df_decorator(dx=0.0001):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper

    return func_decorator


@df_decorator(dx=0.01)
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi / 3)
print(df)


# Декорирование стандартным способом
def df_decorator2(dx=0.0001):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper

    return func_decorator


def sin_df2(x):
    return math.sin(x)


# Вариант полный
f = df_decorator2()
sin_df21 = f(sin_df2)
df = sin_df21(math.pi / 3)
print(df)

# Вариант сокращенный
sin_df22 = df_decorator2(dx=0.000001)(sin_df2)
df = sin_df22(math.pi / 3)
print(df)


# Проблема потери имени и описание декорируемой функции и варианты ее решения
# 1. Через __name__ и __doc__
def df_decorator3(dx=0.0001):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # хороший тон при декорировании функций
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return func_decorator


@df_decorator3(dx=0.001)
def sin_df3(x):
    """Функция вычисления производной синуса"""
    return math.sin(x)


print(sin_df3.__name__)
print(sin_df3.__doc__)

# 2. Через functools и wraps
from functools import wraps


def df_decorator4(dx=0.0001):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # хороший тон при декорировании функций
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper

    return func_decorator


@df_decorator4(dx=0.001)
def sin_df4(x):
    """Функция вычисления производной синуса"""
    return math.sin(x)


print(sin_df4.__name__)
print(sin_df4.__doc__)

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# def st_val_dec(start_value):
#     def st_val(func):
#         @wraps(func)
#         def wrapper(*args):
#             return start_value + func(*args)
#         return wrapper
#     return st_val
#
#
# @st_val_dec(5)
# def str2sum(s):
#     return sum(list(map(int, s.split())))
#
#
# str1 = input()
# print(str2sum(str1))


# Task 2
# def df_get_tagged(tag='h1'):
#     def get_tagged(func):
#         def wrapper(*args):
#             return f"<{tag}>{func(*args)}</{tag}>"
#         return wrapper
#     return get_tagged
#
#
# def str_lower(s):
#     return s.lower()
#
#
# s1 = input()
# str_lower = df_get_tagged(tag='div')(str_lower)
# print(str_lower(s1))


# Task 3
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def df_format_slug(chars=" !?"):
    def format_slug(func):
        def wrapper(*args):
            s = func(*args)
            for x in chars:
                s = s.replace(x, '-')
            while "--" in s:
                s = s.replace("--", "-")
            return s
            # return "-".join(filter(None, s.split('-')))

        return wrapper

    return format_slug


@df_format_slug("?!:;,. ")
def get_slug(s):
    lst = [t.get(char, char) for char in s.lower()]
    return "".join(lst)


# s1 = input()
s1 = "Декораторы - это круто!"
print(get_slug(s1))


# Task 4
def sum_lst(func):
    @wraps(func)
    def wrapper(*args):
        return sum(func(*args))

    return wrapper


@sum_lst
def str2list(s):
    """Функция для формирования списка целых значений"""
    return list(map(int, s.split()))


str1 = input()
print(str2list(str1))
print(str2list.__name__)
print(str2list.__doc__)
