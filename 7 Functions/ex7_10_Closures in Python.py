# 7.10 Замыкания в Python. Вложенные функции
# Closures

print("""
# стандартное определение функции с вложенной функцией: """)


def say_name(name):
    def say_goodbye():
        print("Don't say me goodbye, " + name + "!")

    say_goodbye()


say_name("Sergey")


print("""
# через return - замыкание: """)


def say_name1(name):
    def say_goodbye():
        print("Don't say me goodbye, " + name + "!")

    return say_goodbye


# Функция f держит всю цепочку функций с локальными окружениями.
# У каждой внутренней функции есть ссылка на внешнее окружение.
# Так как есть глобальная ссылка на внутреннее окружение функции,
# то продолжает существовать локальное окружение и вся цепочка внешних окружений, пока существует ссылка f.
# Это называется ЗАМЫКАНИЕМ
f = say_name1("Sergey")
f()

# создание новых экземпляров локальных окружений
f1 = say_name1("Dmitry")
f2 = say_name1("Python")
f1()
f2()


print("""
# счетчик
# используется nonlocal
# замыкание - ссылка на внутреннюю функцию с определенным параметром: """)


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = counter(10)
c2 = counter()
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())

print("""
# Без ссылки значение переменной не поддерживается: """)
print(counter(100)())
print(counter(100)())
print(counter(100)())


print("""
# Замыкание со ссылкой на параметры работы внешней функции
# Вызов ссылки с параметрами работы внутренней функции
# Работа функции strip от строки - перечня удаляемых элементов: """)


def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(" !?,.;")

print(strip1(" hello python!.. "))
print(strip2(" hello python!.. "))

print("""
---------- ЗАДАЧИ ------------""")


# Task 1
# def counter_add():
#     def augment(number):
#         return number + 5
#
#     return augment
#
#
# cnt = counter_add()
# k = int(input())
# print(cnt(k))


# Task 2
# def counter_add(n):
#     def augment(number):
#         return number + n
#
#     return augment
#
#
# cnt = counter_add(2)
# k = int(input())
# print(cnt(k))


# Task 3
# def get_tagged(tag='h1'):
#     def insert_tag(s):
#         return f"<{tag}>{s}</{tag}>"
#
#     return insert_tag
#
#
# # Сокращенная запись
# # print(get_tagged()(input()))
#
# # Базовый вариант - с замыканием (поддерживаемой ссылкой):
# tg1 = get_tagged()
# str1 = input()
# print(tg1(str1))


# Task 4
# def get_tagged(tag):
#     def insert_tag(s):
#         return f"<{tag}>{s}</{tag}>"
#
#     return insert_tag
#
#
# # Сокращенная запись
# # print(get_tagged(input())(input()))
#
# # Базовый вариант - с замыканием (поддерживаемой ссылкой):
# tag1, str1 = input(), input()
# t = get_tagged(tag1)
# print(t(str1))


# Task 5
# sequence to list or tuple

# # Variant 1 - мой базовый вариант, с тернарным условием
# def group(tp):
#     def convert_lst(lst):
#         return list(lst) if tp == 'list' else tuple(lst)
#     return convert_lst
#
#
# print(group(input())(list(map(int, input().split()))))
#
#
# # Variant 2
# def parse(tp='list'):
#     def inner(s):
#         return (tuple, list)[tp == 'list'](map(int, s.split()))
#     return inner
#
#
# pr = parse(input())
# print(pr(input()))
#
#
# # Variant 3
# def parse1(tp='list'):
#     return lambda s: (tuple, list)[tp == 'list'](map(int, s.split()))
#
#
# pr = parse1(input())
# print(pr(input()))


# Variant 4
# def get_lst_tpl(tp):
#     return lambda s: (tuple, list)[tp == 'list'](map(int, s.split()))
#
#
# # Сокращенный вариант
# # print(get_lst_tpl(input())(input()))
#
# # С подробным вызовом
# tp1, lst1 = input(), input()
# print(get_lst_tpl(tp1)(lst1))


# # Variant 5 - в одну строчку (для проверки работы lambda-функции с прямым вызовом с аргументами)
# tp1, s1 = input(), input()
# print((lambda tp, s: (tuple, list)[tp == 'list'](map(int, s.split())))(tp1, s1))
