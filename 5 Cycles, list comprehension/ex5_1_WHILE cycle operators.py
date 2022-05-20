# 5.1 Оператор цикла while

import timeit
N = 1000

# простой цикл
s = 0
i = 1
while i <= N:
    s += i
    i += 1
print(s)

# сложные условия
s = 0
i = 1
while i <= N and i <= 50:
    s += i
    i += 1
print(s)

# 1, 3, 5, 7, 9, ...
s = 0
i = 1
while i <= N and i <= 50:
    s += i
    i += 2
print(s)

# операторы < и > работают быстрее, чем <= и >=
s = 0
i = 1
while i < 10:
    print(i)
    i += 1

N = -10
i = -1
while i >= N:
    print(i)
    i *= 2

# pass_true = "password"
# ps = ""
# while ps != pass_true:
#     ps = input("Введите пароль: ")
# print("Вход в систему")

N = 20
i = 1
while i <= N:
    if i % 3 == 0:
        print(i)
    i += 1

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# # Variant 1
# n, m = map(int, input().split())
# while n <= m:
#     print(n ** 2, end=' ')
#     n += 1
# # Variant 2
# n, m = map(int, input().split())
# l=[]
# while n <= m:
#     l.append(n ** 2)
#     n=n+1
# print(*l)

# Task 6
# С измерением скорости работы алгоритма
# Variant 1
# slug = list(input())

# code_to_test1 = """
# slug = list("osnovnye--metody-----slovarey")
# i = 0
# while i < len(slug) - 1:
#     if slug[i] == '-':
#         while slug[i + 1] == '-':
#             del slug[i + 1]
#     i += 1
# print(''.join(slug))
# """
# elapsed_time1 = timeit.timeit(code_to_test1, number=10000)/10000
# # Variant 2
# code_to_test2 = """
# s1 = "osnovnye--metody-----slovarey"
# while '--' in s1:
#     s1 = s1.replace('--', '-')
# print(s1)
# """
# elapsed_time2 = timeit.timeit(code_to_test2, number=10000)/10000
# print(elapsed_time1)
# print(elapsed_time2)

# Task 7
# # Variant 1
# num = input()
# i = 0
# res = 1
# while i < len(num):
#     res *= int(num[i])
#     i += 1
# print(res)
# # Variant 2
# a, m = list(map(int, input())), 1
# while a:
#     m *= a.pop()
# print(m)

# # Task 9
# n = int(input()) // 3
# print(n)
# i = 1
# s = 1
# while i < n:
#     s = s * 2
#     i += 1
# print(s)

# Task 10
# Variant 1
# r = 0.05
# d = 1000
# i = 0
# n = int(input())
# while i < n:
#     d = d * (1 + r)
#     i += 1
# print(round(d, 2))
# # Variant 2
# years = int(input())
# deposit = 1000
# while years:
#     deposit *= 1.05
#     years -= 1
# print(round(deposit, 2))

# # Task 11
# n, m = map(int, input().split())
# if n % 2 == 0:
#     n += 1
# if m % 2 == 0:
#     m -= 1
# while n <= m:
#     print(n, end=' ')
#     n += 2

# Task 12
i = 99
while i < 1000:
    if i % 47 == 43:
        print(i, end=' ')
    i += 3
