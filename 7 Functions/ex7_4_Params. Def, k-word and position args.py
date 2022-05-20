# 7.4 Именованные аргументы. Фактические и формальные параметры
# Parameters. Default, keyword and position arguments.py

from time import time

# параметры без начальных значений - фактические
# с указанными начальными значениями - формальные (default parameters)
# при вызове функции формальные параметры прописывать не обязательно
def get_v(a, b, c, verbose=True):
    if verbose:
        print(f"a = {a}, b = {b}, c = {c}")
    return a * b * c


# позиционная запись аргументов (positional arguments)
v = get_v(1, 2, 3)
print(v)

# именованная запись аргумента (keyword arguments)
v = get_v(b=1, a=2, c=3)
print(v)

# смешанная запись, сначала должны идти позиционные аргументы, затем именованные
v = get_v(1, c=2, b=3)
print(v)

# смешанная запись, сначала должны идти позиционные аргументы, затем именованные
v = get_v(1, 2, c=3)
print(v)

# необязательное указание формальных параметров
# формальные параметры определяют наиболее частое используемое поведение функции
v = get_v(1, 2, 3, verbose=False)
v = get_v(1, 2, 3, False)
print(v)


def cmp_str(s1, s2, reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()

    return s1 == s2


print(cmp_str('Python', ' Python'))
print(cmp_str('Python', ' Python', trim=False))
print(cmp_str('PYTHON', ' Python'))
print(cmp_str('PYTHON', ' Python', reg=True))


# нюанс при объявлении функции с формальными параметрами
def add_value(value, lst=[]):
    lst.append(value)
    return lst


# формальный параметр с изменяемым типом переменной всегда ссылается на одну и ту же переменную (с одним адресом)
l = add_value(1)
l = add_value(2)
print(l)


# исправленная запись по подсказке PyCharm
def add_value2(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst


# так сохраняется формальный параметр и нужное поведение функции
l2 = add_value2(1)
l2 = add_value2(2)
print(l2)

l3 = add_value2(1)
l3 = add_value2(2, l3)
print(l3)

# этот нюанс существует при определении формальных параметров функции на изменяемые объекты:
# списки, словари, множества

# Задачи
print("\n", "Задачи", sep='')

# Task 2
# # Variant 1
# def get_rect_value(a, b, type=0):
#     if type == 0:
#         return 2 * (a + b)
#     else:
#         return a * b
#
#
# print(get_rect_value(5, 10))
# print(get_rect_value(5, 10, 1))
# # Variant 2
# def get_rect_value(a, b, type=0):
#     return a * b if type else 2 * (a + b)


# Task 3
# # Variant 1
# def check_password(s, chars='$%!?@#'):
#     fl = False
#     if len(s) > 8:
#         for c in s:
#             if c in chars:
#                 fl = True
#                 break
#     return fl
# # Variant 2
# def check_password(s, chars='$%!?@#'):
#     return (set(s) & set(chars)) > set() and len(s) > 7
# # Variant 3
# def check_password(str, chars="$%!?@#"):
#     return len(set(str) & set(chars)) != 0 and len(str) > 7
# # Variant 4
# def check_password(password):
#     return bool(set(password) & set('$%!?@#')) and len(password) > 7
#
#
# print(check_password(';asldkjgqowuieryoqiuerghlasdkjhz,xcmbvaljkhdgfpweriuty438795ou34rtlkjrhfg,.dmfnvb'))
# print(check_password(';asl#dkjgqowuieryoqiuerghlasdkjhz,xcmbvaljkhdgfpweriuty438795ou34rtlkjrhfg,.dmfnvb'))


# Task 4 - real slug function
# # Variant 1
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
# # третий по скорости
# def get_slug(s, sep='-'):
#     slug = "".join([t[x] if x in t else x for x in s.lower()])
#     return sep.join(slug.split())
#
#
# # самый медленный
# def get_slug2(s, sep='-'):
#     lst = []
#     for x in s.lower():
#         if x == ' ':
#             lst.append(sep)
#         elif x in t:
#             lst.append(t[x])
#         else:
#             lst.append(x)
#     return "".join(lst)
#
#
# # Самый быстрый вариант
# def get_slug3(s, sep='-'):
#     return "".join([t[x] if x in t else x for x in s.lower()]).replace(' ', sep)
#
#
#
# s1 = input()
#
# start1 = time()
# for i in range(1000000):
#     s2 = get_slug(s1)
# end1 = time()
# print('1 = ', end1 - start1)
# print(get_slug(s1))
# print(get_slug(s1, sep='+'))
#
# start2 = time()
# for i in range(1000000):
#     s2 = get_slug2(s1)
# end2 = time()
# print('2 = ', end2 - start2)
# print(get_slug2(s1))
# print(get_slug2(s1, sep='+'))
#
# start3 = time()
# for i in range(1000000):
#     s2 = get_slug3(s1)
# end3 = time()
# print('3 = ', end3 - start3)
# print(get_slug3(s1))
# print(get_slug3(s1, sep='+'))
#
# # Variant fin
# # t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
# #      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
# #     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
# #     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
# # второй по скорости
# def get_slug4(s, sep='-'):
#     return "".join([t.get(x, x) for x in s.lower()]).replace(' ', sep)
#
#
# # s1 = input()
# print(get_slug4(s1))
# print(get_slug4(s1, sep='+'))
#
# start4 = time()
# for i in range(1000000):
#     s2 = get_slug4(s1)
# end4 = time()
# print('4 =', end4 - start4)
# print(get_slug4(s1))
# print(get_slug4(s1, sep='+'))

# Task 5
# def get_tagged(s, tag='h1'):
#     return f"<{tag}>{s}</{tag}>"
#
#
# line = input()
# print(get_tagged(line))
# print(get_tagged(line, tag='div'))

# Task 6
# def get_tagged(s, tag='h1', up=True):
#     if up:
#         tag = tag.upper()
#     return f"<{tag}>{s}</{tag}>"
#
#
# line = input()
# print(get_tagged(line, tag='div'))
# print(get_tagged(line, tag='div', up=False))
