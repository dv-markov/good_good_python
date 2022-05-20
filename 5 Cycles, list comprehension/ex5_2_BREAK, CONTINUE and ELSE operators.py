# 5.2 Операторы break, continue и else

print("Запуск цикла")
i = 0
while True:
    i += 1
    break
print("Завершение цикла")

# break - досрочный выход из цикла
d = [1, 5, 3, 6, 0, -4]
flFind = False
i = 0
while i < len(d):
    print(i)
    flFind = d[i] % 2 == 0
    if flFind:
        break
    i += 1
print(flFind)

# без break - более сложный для понимания действий цикла алгоритм
flFind = False
i = 0
while i < len(d) and d[i] % 2 != 0:
    i += 1
flFind = i != len(d)
print(flFind)

# подсчет суммы всех введенных нечетных значений
# оператор continue - досрочный выход из итерации
# позволяет сделать текст цикла более читаемым
# s = 0
# d = 1
# while d != 0:
#     d = int(input("Введите целое число: "))
#     if d % 2 == 0:
#         continue
#     s += d
#     print(("s = " + str(s)))

# оператор else цикла while
# выполняется только после штатного завершения работы цикла
# можно проверять для проверки корректного выполнения цикла
# S = 1/2 + 1/3 + 1/4 + 1/10 + ... + 1/0
S = 0
i = -10
while i < 0:
    if i == 0:
        break
    S += 1 / i
    i += 1
else:
    print("Сумма вычислена корректно")
print(S)

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# Variant 1
# p = [0] * 10
# i = 0
# while i < 5:
#     j = int(input())
#     if p[j] == 1:
#         continue
#     p[j] = 1
#     i += 1
# print(*p)
# # Variant 2
# p = [0] * 10
# while p.count(1) < 5:
#     num = int(input())
#     if p[num] == 1:
#         continue
#     p[num] = 1
# print(*p)

# Task 2
# # Variant 1
# s = 1
# d = 1
# while d != 0:
#     d = int(input())
#     if d <= 0:
#         continue
#     s *= d
# print(s)
# # Variant 2
# res, x = 1, 1
# while x:
#     x = int(input())
#     if x <= 0:
#         continue
#     res *= x
# print(res)

# Task 5
# # Variant 1
# lst = input().split()
# i = 0
# while i < len(lst):
#     if lst[i].lower()[0] == lst[i].lower()[-1]:
#         print("ДА")
#         break
#     i += 1
# else:
#     print("НЕТ")
# # Variant 2
# lst = input().split()
# flag = "НЕТ"
# count = 0
# while count < len(lst):
#     if lst[count][0].lower() == lst[count][-1].lower():
#         flag = 'ДА'
#         break
#     count += 1
# print(flag)

# # Task 6
# n = int(input())
# i = 1
# s = ''
# while i <= n:
#     if i % 3 == 0 and i % 5 == 0:
#         s = s + str(i) + ' '
#     i += 1
# else:
#     if n >= 100:
#         s = 'слишком большое значение n'
# print(s)

# # Task 7
# n = int(input())
# i = 1
# while i ** 2 <= n:
#     i += 1
# print(i)

# # Task 8
# x = int(input())
# dist = 10
# i = 1
# while dist <= x:
#     dist *= 1.1
#     i += 1
# print(i)

# # Task 9
# # Variant 1
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(lst_in)
# # здесь продолжайте программу (используйте список lst_in)
# i = 0
# while i < len(lst_in):
#     if ' ' in lst_in[i]:
#         del lst_in[i]
#         continue
#     i += 1
# print(*lst_in)
# # Variant 2
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# i=0
# while i<len(lst_in):
#     if len(lst_in[i].split())==1:
#         print(lst_in[i], end=' ')
#     i+=1

