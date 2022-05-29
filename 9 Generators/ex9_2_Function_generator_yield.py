# 9.2 Функция-генератор. Оператор yield

# обычная функция
def get_list():
    for x in [1, 2, 3, 4]:
        return x


a0 = get_list()
print(a0)


# оператор yield
# yield превращает любую функцию в генератор
def get_list1():
    for x in [1, 2, 3, 4]:
        yield x


a1 = get_list1()
print(a1)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

for k in a1:
    print(k)


# вычисление среднего арифметического для убывающего списка
def get_list2():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)


a2 = get_list2()
print(list(a2))


# получение данных из файла через генератор
def find_word(f, word):
    g_indx = 0
    for line in f:
        indx = 0
        while indx != -1:
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1
        g_indx += len(line)


try:
    with open("lesson_54.txt", encoding="utf-8") as file:
        a = find_word(file, "генератор")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Ошибка при работе с файлом")


print("""
# Задачи
""")


# Task 1
# N = int(input())
#
#
# # # Variant 1
# # def get_sum(n):
# #     for i in range(1, n+1):
# #         s1 = 0
# #         for j in range(i, 0, -1):
# #             s1 += j
# #         yield s1
#
#
# # Variant 2
# def get_sum(n):
#     s1 = 0
#     for i in range(1, n+1):
#         s1 += i
#         yield s1
#
#
# s = get_sum(N)
# for k in range(N):
#     print(next(s), end=' ')


# Task 2
# # Variant 1
# def bal_gen(n):
#     el1 = el2 = el3 = 1
#     for i in range(n):
#         if i < 3:
#             yield 1
#         else:
#             summ = el1 + el2 + el3
#             el1 = el2
#             el2 = el3
#             el3 = summ
#             yield el3
#
#
# N = int(input())
# # N = 10
# b = bal_gen(N)
# for k in range(N):
#     print(next(b), end=' ')

# Variant 2
# N = int(input())
N = 10


def get_sum(N):
    a = b = c = 1
    for _ in range(N):
        yield a
        a, b, c = b, c, a + b + c


print(*get_sum(N))


# Task 3
import random
from string import ascii_lowercase, ascii_uppercase

random.seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"


def pass_gen(n):
    res = []
    for i in range(n):
        indx = random.randint(0, len(chars) - 1)
        res.append(chars[indx])
    yield ''.join(res)


N = 10
# N = int(input())
for k in range(5):
    print(next(pass_gen(N)))


# Task 4
import random
from string import ascii_lowercase, ascii_uppercase

random.seed(1)
chars = ascii_lowercase + ascii_uppercase


def email_gen(n):
    res = []
    for i in range(n):
        indx = random.randint(0, len(chars) - 1)
        res.append(chars[indx])
    yield ''.join(res) + '@mail.ru'


N = 8
# N = int(input())
for k in range(5):
    print(next(email_gen(N)))


# Task 5

# def prime_gen():
#     p = 1
#     while True:
#         p += 1
#         # for x in range(2, int(p ** 0.5) + 1):
#         for x in range(1, p):
#             if p % x == 0:
#                 break
#         yield p

def prime_gen():
    for i in range(2, 100):
        # for j in range(2, int(i ** 0.5) + 1):
        #     if i % j == 0:
        #         break
        yield i


print(next(prime_gen()))
print(next(prime_gen()))
print(next(prime_gen()))

# print(prime_gen())
# print(prime_gen())

# for i in range(2, 100):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

