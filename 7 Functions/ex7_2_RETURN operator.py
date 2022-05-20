# 7.2 Оператор return. Функциональный подход к программированию.

def send_mail1(from_name, age):
    text = f"""Уважаемый Сергей Балакирев!
    Я так и не понял, что такое функция.
    Объясните лучше!
    Ваш, навсегда {from_name}! И не судите строго, мне всего {age} лет!"""

    print(text)


def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res
    # после первого оператора return функция завершает свою работу
    return x  # этот оператор не будет выполнен


a1 = get_sqrt(49)
print(a1)


# вернуть две переменные можно через кортеж или любую другую коллекцию
def get_sqrt1(x):
    res = None if x < 0 else x ** 0.5
    return res, x  # возвращение кортежа


a1, b1 = get_sqrt1(49)
print(a1, b1)


def get_max2(a, b):
    return a if a > b else b


def get_max3(a, b, c):
    return get_max2(a, get_max2(b, c))


x1, y1 = 5, 7
print(get_max2(x1, y1))

x1, y1, z1 = 5, 7, 10
print(get_max2(x1, get_max2(y1, z1)))

# определение функции по условию
PERIMETER = False
if PERIMETER:
    def get_rect(a, b):
        return 2 * (a + b)
else:
    def get_rect(a, b):
        return a * b

print(get_rect(1.5, 3.8))


def even(x):
    return x % 2 == 0


# функцию можно вызывать в любом месте программы, где это необходимо
for i in range(1, 20):
    if even(i):
        print(i)


# Задачи
print("\n", "Задачи", sep='')


# Task 1
# def sq(x):
#     return x ** 2
#
#
# print(sq(float(input())))

# Task 2
# # Variant 1
# def is_triangle(a, b, c):
#     return 2 * max(a, b, c) < a + b + c
#
#
# x, y, z = map(int, input().split())
# print(is_triangle(x, y, z))
# # Variant 2
# def is_triangle(a, b, c):
#     a, b, c = sorted((a, b, c)) # в скобках кортеж
#     return c < a + b

# Task 3
# def is_large(s):
#     return len(s) > 2
#
# print(is_large(input()))

# Task 4
# def is_even(x):
#     return x % 2 == 0
#
#
# n = int(input())
# while n != 1:
#     if is_even(n):
#         print(n)
#     n = int(input())

# Task 5
# def is_odd(x):
#     return x % 2
#
#
# lst = [x for x in input().split() if is_odd(int(x))]
# print(*lst)

# Task 6
# tp = input().strip()
#
# if tp == 'RECT':
#     def get_sq(a, b):
#         return a * b
# else:
#     def get_sq(a):
#         return a * a
#
# print(get_sq(int(input())))

# Task 7
# def is_longer5(s):
#     return len(s) > 5
#
#
# cities = input().split()
# lst = [x for x in cities if is_longer5(x)]
# print(*lst)

# Task 8 - первое применение лямбда-функции
# Variant 1
# def str_len(s):
#     return s, len(s)
#
#
# d = {str_len(x)[0]: str_len(x)[1] for x in input().split()}
# a = sorted(d, key=lambda x: d[x])
# print(*a)
# Variant 2
# def get_len(s):
#     return s, len(s)
#
#
# # кортеж для элемента словаря воспринимается как ключ: значение
# d = dict(get_len(i) for i in input().split())
# print(*sorted(d, key=lambda x: d[x]))

# Task 9
# def get_mplied(a, b):
#     return a * b
#
#
# lst = list(map(int, input().split()))
# print(get_mplied(max(lst), min(lst)))

