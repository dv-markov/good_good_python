# 9.5 Функция zip

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]

z = zip(a, b)
print(z)
print(next(z))
print(next(z))

for x in z:
    print(x)

# расход памяти увеличивается при преобразовании итератора в кортеж
z = tuple(zip(a, b))
print(z)

c = "python"
z = zip(a, b, c)
# итератор останавливается на самом короткой объекте
for x in z:
    print(x)

z = zip(a, b, c)
for v1, v2, v3 in z:
    print(v1, v2, v3)

# количество элементов для распаковки должно соответствовать количеству шагов итератора
z1, z2, z3, z4 = zip(a, b, c)
print(z1, z2, z3, z4)

# или остальные позиции надо упаковывать в переменную со *
z1, *z2 = zip(a, b, c)
print(z1, z2)

# перераспределение значений через zip
z = zip(a, b, c)
lz = list(z)
print(*lz)
t1, t2, t3 = zip(*lz)
print(t1, t2, t3, sep="\n")

# аналог
z = zip(a, b, c)
t1, t2, t3 = zip(*z)
print(t1, t2, t3, sep="\n")

print("""
Задачи
""")

# Task 1

# Variant 1
# l1 = input().split()
# l2 = input().split()
l1 = '-7 8 11 -1 3'.split()
l2 = '1 2 3 4 5 6 7 8 9 10'.split()
z = zip(l1, l2)
# print(*z)
res = map(lambda x: int(x[0]) * int(x[1]), z)
# print(*res)
print(*(next(res) for _ in range(3)))

# Variant 2
# lst1 = map(int, input().split())
# lst2 = map(int, input().split())
lst1 = map(int, l1)
lst2 = map(int, l2)
lst = map(lambda x, y: x * y, lst1, lst2)
print(*(next(lst) for _ in range(3)))


# Task 2

# Variant 1
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst = [x.split() for x in lst_in]
# z1 = zip(*lst)
# z2 = zip(*z1)
# for x in z2:
#     print(*x)

# Variant 2
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # здесь продолжайте программу (используйте список строк lst_in)
# list(map(print, *zip(*map(str.split, lst_in))))

# Task 3
# Variant 1
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(lst_in)
# z = zip(*map(str.split, lst_in))
# for x in z:
#     print(*x)
# # Variant 2
# [print(*i) for i in zip(*map(str.split, lst_in))]

# Пример совмещения итератора и zip
# для деления линейного списка на матрицу с произвольным количеством столбцов
x = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(*zip(x, x, x))

# Task 4
# lst = input().split()
lst_in = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'
lst0 = lst_in.split()
# решение со срезами
# lst = [lst0[i:i+3] for i in range(0, len(lst0), 3)]
# print(*lst[0:3])
# решение с zip
z = zip(*[iter(lst0)]*3)
for x in z:
    print(*x)

# Task 5
# s = input()
s = 'Python дай мне силы пройти этот курс до конца!'
N = 10

en = list(enumerate(s[:N]))
print(en)

lst = list(zip(s, range(N)))
print(lst)
