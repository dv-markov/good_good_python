# 7.1 Что такое функции. Их объявление и вызов

# описание функции (ссылка на объект-функцию)
# print

# вызов функции
print()

# ссылка другого имени функции на тот же объект-функцию
f = print
f('привет, как дела?', '\n')


# print = 'это была функция print'
# f(print)

# DRY - Don't Repeat Yourself
# функции были введены для устранения дублирования кода
# имя функции обычно содержит глагол, имена функции должны быть понятными

def send_mail():
    text = "Уважаемый Сергей Балакирев! Я так и не понял, что такое функция. Объясните лучше!"
    print(text)


# определение переменной при объявлении функции - параметр
def send_mail1(from_name, age):
    text = f"""Уважаемый Сергей Балакирев!
    Я так и не понял, что такое функция.
    Объясните лучше!
    Ваш, навсегда {from_name}! И не судите строго, мне всего {age} лет!"""

    print(text)


# Объявление функции и текст программы отделяются двумя пустыми строками
# Вызов функции должен идти после ее объявления
send_mail()
send_mail()

# переменная при вызове функции - аргумент
send_mail1("Иван Иванович", 56)


# Задачи
print("\n", "Задачи", sep='')

# Task 3
# def mff():
#     print("It's my first function")
# mff()

# Task 4
# def task_done():
#     name = input()
#     print(f"Уважаемый, {name}! Вы верно выполнили это задание!")
# task_done()

# Task 5
# def tell_weight(weight):
#     print(f"Предмет имеет вес: {weight} кг.")
# w = input()
# tell_weight(w)

# Task 6
# def characterize_list(lst):
#     print(f"Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}")
# lst_n = list(map(int, input().split()))
# characterize_list(lst_n)

# Task 7
# def rect_perimeter(width, height):
#     print("Периметр прямоугольника равен", width * 2 + height * 2)
# # w, h = input().split()
# # rect_perimeter(int(w), int(h))
# w, h = [int(x) for x in input().split()]
# rect_perimeter(w, h)

# Task 8
#
# print('a =', ord('a'))
# print('z =', ord('z'))
# print('A =', ord('A'))
# print('Z =', ord('Z'))
# print('0 =', ord('0'))
# print('9 =', ord('9'))
# print('_ =', ord('_'))
# for i in range(48, 123):
#     print(f'chr({i}) = {chr(i)}')
#
# # Variant 1
#
#
# def verify_eml(eml):
#     fl = False
#     if ('@' and '.') in eml:
#         set_eml = {ord(x) for x in eml if x not in '@.'}
#         if set_eml < set(range(48, 57)) | set(range(65, 91)) | set(range(97, 123)) | {95}:
#             fl = True
#     print(('НЕТ', 'ДА')[fl])
#
#
# verify_eml(input())
#
# # print(set(range(48, 58)) | set(range(65, 91)) | set(range(97, 123)) | {95})
# # print(type({95}))  # это множество

# # Variant 2 - качественный алгоритм в рамках темы
# t = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'
#
#
# def mail_check(mail):
#     print("ДА" if mail.count('@') == 1 and mail.count('.') == 1 and (mail[0] and mail[-1] not in t[-3:]) and set(
#         mail) <= set(t) else "НЕТ")
#
#
# mail_check(input().lower())

# Variant 3 - быстрый алгоритм со сторонней библиотекой
# import re
#
#
# def check_email(email):
#     regex = r'[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}'
#     print('ДА' if re.fullmatch(regex, email) else 'НЕТ')
#
#
# check_email(input())

# Проверка алгоритмов на скорость
#
# from time import time
#
# start1 = time()
# for i in range(10000):
#
#     def verify_eml(eml):
#         fl = False
#         if ('@' and '.') in eml:
#             set_eml = {ord(x) for x in eml if x not in '@.'}
#             if set_eml < set(range(48, 57)) | set(range(65, 91)) | set(range(97, 123)) | {95}:
#                 fl = True
#         print(('НЕТ', 'ДА')[fl])
#     verify_eml('sc_lib@list.ru')
# end1 = time()
#
#
# start2 = time()
# for i in range(10000):
#     t = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'
#
#     def mail_check(mail):
#         print("ДА" if mail.count('@') == 1 and mail.count('.') == 1 and (mail[0] and mail[-1] not in t[-3:]) and set(
#             mail) <= set(t) else "НЕТ")
#     mail_check('sc_lib@list.ru'.lower())
# end2 = time()
#
#
# import re
# start3 = time()
# for i in range(10000):
#     def check_email(email):
#         regex = r'[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}'
#         print('ДА' if re.fullmatch(regex, email) else 'НЕТ')
#     check_email('sc_lib@list.ru')
# end3 = time()
#
# print(end1 - start1)
# print(end2 - start2)
# print(end3 - start3)


