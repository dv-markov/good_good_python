# 4.1 Условный оператор if. Конструкция if-else

# синтаксис отнесения операторов к условию - единый отступ, по умолчанию 4 пробела
# x = -4
# if x < 0:
#     x = -x
# print(x)
#
# a = float(input("a: "))
# b = float(input("b: "))
# if a < b:
#     a, b = b, a
# print(a, b)

# x = int(input("Введите х: "))
# if x >= -4 and x <= 10:
#     print("x в диапазоне от [-4; 10]")
# # упрощенная запись
# if -4 <= x <= 10:
#     print("x в диапазоне от [-4; 10]")
#
# # условие истинно, если переменная ссылается на непустой объект (непустое значение)
# if x:
#     print("x True")

# marks = [3, 3, 4, 4, 4]
# if 2 in marks:
#     print("Студент будет отчислен")
# else:
#     print("Студент успешно сдал сессию")

# x = int(input())

# if x < 0:
#     print("x - отрицательное число")
# else:
#     print("x - неотрицательное число")

# if x % 2 == 0:
#     print("x - четное число")
# else:
#     print("x - нечетное число")

# Задачи
print("\n", "Tasks", sep='')
# Task 1
# # Variant 1
# a, b = map(float, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)
# # Variant 2
# # аналог условного оператора
# a, b = [float(i) for i in input().split()]
# print((a, b)[b > a])

# Task 2
# # Variant 1
# a = input().lower()
# if a == a[::-1]:
#     print("ДА")
# else:
#     print("НЕТ")
# # Variant 2
# a = input().lower()
# print(['НЕТ', 'ДА'][a == a[::-1]])

# Task 3
# m, n = map(int, input().split())
# if m % n == 0:
#     print(m//n)
# else:
#     print(f'{m} на {n} нацело не делится')

# Task 4
# a, b, c = map(int, input().split())
# if a**2 + b**2 == c**2:
#     print('ДА')
# else:
#     print('НЕТ')

# Task 5
# a = input()
# if a[-1] == '7':
#     print('ДА')
# else:
#     print('НЕТ')

# Task 7
# cities = input().split()
# if 'Москва' in cities:
#     cities.remove('Москва')
# print(*cities)

# Task 8
# a, b, c, d = map(int, input().split())
# if (a - 2 >= c and b - 2 >= d) or (b - 2 >= c and a - 2 >= d):
#     print('ДА')
# else:
#     print('НЕТ')

# test
lst = [10, 2, 3]
print(sum(lst), lst[0], '\n')
s1 = "123"
l1 = list(map(int, s1))
print(l1)

# Task 9
# Подвиг 9. Вводится шестизначное число. Определить, является ли оно счастливым.
# (Счастливым называют такое шестизначное число, в котором сумма его первых трех цифр
# равна сумме его последних трех цифр.). Вывести ДА, если счастливое и НЕТ - в противном случае.
# num = list(map(int, input()))
# if sum(num[:3]) == sum(num[3:]):
#     print('ДА')
# else:
#     print('НЕТ')

# Task 10
# Variant 1
# t = float(input())
# if t % 5 <= 3:
#     print("green")
# else:
#     print("red")
# Variant 2
# print(('green', 'green', 'green', 'red', 'red')[int(float(input())) % 5])
# Variant 3
# print((['green']*3 + ['red']*2)[int(float(input())) % 5])
