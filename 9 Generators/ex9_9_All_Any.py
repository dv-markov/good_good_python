# 9.9 Функции all и any

# если все эелементы списка принимаются значение Истина, функция all возвращает значение Истина
a = [True, True, True, True]

b = all(a)
print(b)

a[2] = False
print(all(a))

c = [0, 1, 2.5, "", "python", [], [1, 2], {}]
print(all(c))

# все элементы перед оценкой функцией all превращаются в тип bool

# все пустое является ложью
print(bool(0))
print(bool([]))
print(bool({}))

# не пустое - True
print(bool(1))
print(bool([1, 2]))

d = [1, 2.5, "python", [1], [1, 2]]
print(all(d))

# имитация работы функции all
all_res = True
for x in a:
    all_res = all_res and bool(x)

print(all_res)

print("""
Функция any""")
# функция any - возвращает True, если хотя бы одно из значений True
print(any(a))
print(any([False, False, False]))
# возвращает False только, когда все - False

# имитация работы функции any
all_res2 = False
for x in a:
    all_res2 = all_res2 or bool(x)

print(all_res2)

print("""
Пример применения функции all - крестики-нолики:""")

P = ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
print(P)
row_1 = all(map(lambda x: x == 'x', P[:3]))
row_2 = all(map(lambda x: x == 'x', P[3:6]))
row_3 = all(map(lambda x: x == 'x', P[6:]))
print(row_1, row_2, row_3)


# или


def true_x(a):
    return a == 'x'


row_1 = all(map(true_x, P[:3]))
row_2 = all(map(true_x, P[3:6]))
row_3 = all(map(true_x, P[6:]))
print(row_1, row_2, row_3)

col_1 = all(map(true_x, P[::3]))
col_2 = all(map(true_x, P[1::3]))
col_3 = all(map(true_x, P[2::3]))
print(col_1, col_2, col_3)

diag_1 = all(map(true_x, P[::4]))
diag_2 = all(map(true_x, P[2::2]))
print(diag_1, diag_2)

print("""
Пример применения функции any - Сапер:""")
N = 10
P = [0] * (N * N)
print(N)
print(P)

P[4] = '*'

loss = any(map(lambda x: x == '*', P))
print(loss)

print("""
Задачи
""")

# Task 1
lst1 = '2 4 6 8 22 56'.split()
# lst1 = input().split()
print(all(map(lambda x: not int(x) % 2, lst1)))


# Task 2
# lst = map(float, input().split())
# print(any(map(lambda x: x < 0, lst)))


# Task 3
# Variant 1
# def is_string(lst):
#     return all(map(lambda x: type(x) == str, lst))

# Variant 2
def is_string(lst):
    return all(map(lambda x: isinstance(x, str), lst))


print(is_string([1, 2, 3, 'sdfdsf', ' sdfdsf']))
print(is_string(['sdfdsf', ' sdfdsf']))
print(is_string({'lad;kfj; lkj', ';ldkfgj;ldkfjg', 45}))
print(is_string((';slkjfger;gtjl', ';adlkjfrjgt;ijrket')))

# Task 4
# Variant 1
# lst = map(int, input().split())
lst = map(int, '3 3 3 2 3 3'.split())
print(('учится', 'отчислен')[any(map(lambda x: x < 3, lst))])

# Variant 2
# lst = input().split()
lst = '3 3 3 5 3 3'.split()
print(('учится', 'отчислен')[any(map(lambda x: int(x) < 3, lst))])


# Task 5
# # Variant 1
# def is_free(lst):
#     for z in lst:
#         if any(map(lambda y: y == '#', z)):
#             return True
#     return False


# Variant 2
def is_free(lst):
    return any('#' in x for x in lst)


lst1 = ['# x o', 'x # x', 'o o #']
print(is_free(lst1))
