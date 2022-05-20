print("""
        7.9 Области видимости. Ключевые слова global и nonlocal
    """)

# Пространства имен:
# Глобальные переменные - доступны в любом месте программы, внутри всего файла
# Локальные переменные - существуют только внутри функции

N = 100
WIDTH, HEIGHT = 1000, 500


def my_func(lst):
    for x in lst:
        n = x + 1
        print(n)


# # ошибка "переменная не определена"
# print(n)
my_func([1, 2, 3])
# # n не определена даже после вызова функции, потому что она в локальном пространстве имен функции
# print(n)


def my_func2(lst):
    print("Изменение локальной N:", end=' ')
    N = 20
    print(N, WIDTH)
    for x in lst:
        n = x + 1 + N
        print(n)


my_func2([1, 2, 3])
print('Глобальная N:', N)


# доступ к глобальной переменной из функции
def my_func3(lst):
    global N
    print("Изменение глобальной N из функции через global:", end=' ')
    N = 20
    print(N, WIDTH)
    for x in lst:
        n = x + 1 + N
        print(n)


my_func3([1, 2, 3])
print('Глобальная N:', N)


# создание глобальной переменной внутри функции
def my_func4(lst):
    global M
    print("Создание глобальной M из функции через global:", end=' ')
    M = 40
    print(M, WIDTH)
    for x in lst:
        n = x + 1 + M
        print(n)


my_func4([1, 2, 3])
print('Глобальная M, объявленная внутри функции:', M)

print("""
# вложенные функции""")

x = 0


def outer():
    x = 1

    def inner():
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()
print("global: ", x)

print("""
# nonlocal""")

x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()
print("global: ", x)

# nonlocal работает только в функциях, которые вложены в другие функции

print("""
# nonlocal не работает при ссылке внешний функции на global""")


def outer():
    global x
    x = 1
    def inner():
        # nonlocal x
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()
print("global: ", x)

print("""
---------- ЗАДАЧИ ------------""")

# Task 3

# # task
# WIDTH = int(input())
#
#
# def func1():
#     WIDTH += 1
#     return WIDTH
#
#
# print(func1())


# # solution
# WIDTH = int(input())
def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH


print(func1())


# Task 4

# # task
# def func1():
#     msg = input()
#
#     def func2():
#         msg = input()
#         print(msg)
#
#     func2()
#     print(msg)
#
#
# func1()


# # solution
# def func1():
#     msg = input()
#
#     def func2():
#         nonlocal msg
#         msg = input()
#         print(msg)
#
#     func2()
#     print(msg)
#
#
# func1()


# Task 5
def create_global(x):
    global TOTAL
    TOTAL = x


create_global(50000)
print(TOTAL)
