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


df = sin_df(math.pi/3)
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
