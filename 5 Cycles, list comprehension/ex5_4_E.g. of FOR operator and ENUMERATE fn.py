# 5.4 Примеры работы оператора цикла for. Функция enumerate

# вычисление факториала
# n = int(input("Введите натуральное число не более 100: "))
# if n < 1 or n > 100:
#     print("Неверно введено натуральное число")
# else:
#     p = 1
#     for i in range(1, n+1):
#         p *= i
#
#     print(f'Факториал {n}! = {p}')

# елочка
for i in range(1, 7):
    print('*' * i)

# объединение списка в строку с методом lstrip (работает быстрее)
words = ["Python", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
s = ''
for w in words:
    s += ' ' + w
print(s.lstrip())

# объединение списка в строку с флагом (работает более медленно)
words = ["Python", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
s = ''
fl_first = True
for w in words:
    s += ('' if fl_first else ' ') + w
    fl_first = False
print(s)

# объединение списка в строку с методом join (самый быстрый)
words = ["Python", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
print(" ".join(words))

# двузначные числа
digs = [4, 3, 100, -53, -30, 1, 34, -8]
for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99:
        digs[i] = 0
print(digs)

# индекс и значение итерируемого объекта, функция enumerate
digs = [4, 3, 100, -53, -30, 1, 34, -8]
print(list(enumerate(digs)))
for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        digs[i] = 0
print(digs)

# преобразование кириллицы в латиницу
t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
     'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
     'shch', '', 'y', '', 'e', 'yu', 'ya']
start_index = ord('а')
title = "Программирование на Python - лучший курс"
slug = ''
for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s) - start_index]
    elif s == 'ё':
        slug += 'yo'
    elif s in " !?;:.,":
        slug += '-'
    else:
        slug += s
while slug.count('--'):
    slug = slug.replace('--', '-')
print(slug)

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# # Variant 1
# str1 = input().lower()
# if 'ра' in str1:
#     for i in range(len(str1) - 1):
#         if str1[i] + str1[i+1] == 'ра':
#             print(i, end=' ')
# else:
#     print('-1')
# # Variant 2
# st = input()
# count = 0
# while 'ра' in st:
#     print(st.find('ра'), end=' ')
#     st = st.replace('ра', '**', 1)
#     count += 1
# if count == 0:
#     print(-1)
# # Variant 3
# s = input()
# res = [i for i in range(len(s) - 1) if s[i] == 'р' and s[i + 1] == 'а']
# print(*res or [-1])
# # Variant 4 - работает неправильно, если в строке первая буква 'р', а последняя 'а'
# s = input().lower()
# if 'ра' not in s:
#     print(-1)
# else:
#     for i, c in enumerate(s):
#         if c == 'а' and s[i - 1] == 'р':
#             print(i - 1, end=' ')

# Task 2
# str_frmt = '+7(***)***-**-**'
# ph_number = input()
# if len(ph_number) == len(str_frmt):
#     flg = 'ДА'
#     for i, s in enumerate(ph_number):
#         if not ((str_frmt[i] == '*' and s.isdigit()) or (str_frmt[i] != '*' and str_frmt[i] == s)):
#             flg = 'НЕТ'
#             break
# else:
#     flg = 'НЕТ'
# print(flg)

# Task 3
# # Variant 1
# s = input()
# res = eval(s)
# print(res)
# # Variant 2
# text = input().replace(' ', '').replace('-', '+-').split('+')
# print(sum(map(int, text)))
# # Variant 3
# e = map(int, input().replace(' ', '').replace('+', ' +').replace('-', ' -').split())
# print(sum(e))

# Task 4
# lst = list(map(int, input().split()))
# for i, x in enumerate(lst):
#     lst[i] = x ** 2
# print(*lst)

# Task 5
# lst = input().split()
# for x in lst:
#     print(x, x, end=' ')

# Task 6
# lst = list(map(float, input().split()))
# for i in range(len(lst) - 1):
#     if lst[i] < lst[i+1]:
#         lst[i+1] = lst[i]
# print(lst[-1])

# Task 7
# # Variant 1
# lst = input().split()
# for i, x in enumerate(lst):
#     if x[0] == '-':
#         lst[i] = '-1.0'
# print(*lst)
# # Variant 2
# print(*['-1.0' if '-' in c else c for c in input().split()])
# # Variant 3
# print(*('-1.0' if '-' in c else c for c in input().split()))
