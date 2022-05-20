# 4.2 Вложенные условия и множественный выбор

# x = int(input())
# if x % 2 == 0:
#     if 0 <= x <= 9:
#         print("x - цифра")
#     else:
#         print("x - число")
# else:
#     print("x - нечетное число")
#
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a > b:
#     if a > c:
#         print('a -> max')
#     else:
#         print('c -> max')
# else:
#     if b > c:
#         print('b -> max')
#     else:
#         print('c -> max')
# нормальной практикой считается до трех уровней вложения

# Множественный выбор elif
# item = int(input())
# if item == 1:
#     print("Выбран курс по Python")
# elif item == 2:
#     print("Выбран курс по C++")
# elif item == 3:
#     print("Выбран курс по Java")
# elif item == 4:
#     print("Выбран курс по JavaScript")
# else:
#     print("Неверный пункт")

# elif
# x = int(input())
# if x < 0:
#     print("х должно быть положительным")
# elif 0 <= x <= 9:
#     print("х - цифра")
# elif 10 <= x <= 99:
#     print("х - двузначное число")
# elif 100 <= x <= 999:
#     print("х - трехначное число")

# Задачи
print("\n", "Tasks", sep='')

# Task 1
# # Variant 1
# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# mlist = m.split("\n")
# sel = int(input())
# if sel == 1:
#     print(mlist[0])
# elif sel == 2:
#     print(mlist[1])
# elif sel == 3:
#     print(mlist[2])
# elif sel == 4:
#     print(mlist[3])
# elif sel == 5:
#     print(mlist[4])
# elif sel == 6:
#     print(mlist[5])
# # Variant 2
# print(mlist[sel-1])

# Task 2
# a, b, c = map(int, input().split())
# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# elif b < c:
#     print(b)
# else:
#     print(c)

# Task 3
# w = float(input())
# if w <= 60:
#     print(1)
# elif w <= 64:
#     print(2)
# elif w <= 69:
#     print(3)
# else:
#     print(4)

# Task 4
# n = int(input())
# if n == 1:
#     print("понедельник")
# elif n == 2:
#     print("вторник")
# elif n == 3:
#     print("среда")
# elif n == 4:
#     print("четверг")
# elif n == 5:
#     print("пятница")
# elif n == 6:
#     print("суббота")
# elif n ==7:
#     print("воскресенье")

# Task 5
# m = int(input())
# if m == 2:
#     print(28)
# elif m in [4, 6, 9, 11]:
#     print(30)
# else:
#     print(31)

# Task 6
# Variant 1
# m, n = map(int, input().split())
# m30 = [4, 6, 9, 11]
# n1 = n - 1
# n2 = n + 1
# m1 = m
# m2 = m
# # if m == 1:
# #     if n == 31:
# #         n2 = 1
# #         m2 = 2
# #     elif n == 1:
# #         n1 = 31
# #         m1 = 12
# if m == 2:
#     if n == 28:
#         n2 = 1
#         m2 = 3
#     elif n == 1:
#         n1 = 31
#         m1 = 1
# elif m in m30:
#     if n == 30:
#         n2 = 1
#         m2 = m + 1
#     elif n == 1:
#         n1 = 31
#         m1 = m - 1
# elif m == 3:
#     if n == 31:
#         n2 = 1
#         m2 = m + 1
#     elif n == 1:
#         n1 = 28
#         m1 = m - 1
# elif m == 8:
#     if n == 31:
#         n2 = 1
#         m2 = m + 1
#     elif n == 1:
#         n1 = 31
#         m1 = m - 1
# else:
#     if n == 31:
#         n2 = 1
#         m2 = m + 1
#     elif n == 1:
#         n1 = 30
#         m1 = m - 1
# print(f'{str(m1).rjust(2, "0")}.{str(n1).rjust(2, "0")} {str(m2).rjust(2, "0")}.{str(n2).rjust(2, "0")}')

# Variant 2
# m, n = map(int, input().split())
# lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if n == 1:
#     print(f'{m-1:02}.{lst[m-2]} {m:02}.{n+1:02}')
# elif n == lst[m-1]:
#     print(f'{m:02}.{n-1:02} {m+1:02}.01')
# else:
#     print(f'{m:02}.{n-1:02} {m:02}.{n+1:02}')

# testlab
t = 33
print(f'тест {t:07} проверка')
# изучить expressions для f-строк

# Task 7
k = int(input())
lst = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
print(lst[k % 7 - 1])
