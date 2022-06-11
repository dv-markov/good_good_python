# 10.3 Модуль random стандартной библиотеки

import random

# псевдо-случайное число в диапазоне [0.0, 1.0)
# с равномерным распределением
a = random.random()
print(a)

# случайное число в диапазоне от a до b
c = random.uniform(a, 10)
print(c)

# целочисленное случайное значение
# крайнее левое и крайнее правое числа включается в диапазон
b = random.randint(-3, 7)
print(b)

# случайное целое число в диапазоне, опционально с шагом
a = random.randrange(-3, 10, 2)
print(a)

# все вышеприведенные функции дают нормальное распределение
# есть возможность получить нормальное (гауссовское) распределение
# в реальном мире многие события подчиняются именно нормальному распределению
# mu - математическое ожидание (среднее значение СВ)
# sigma - среднеквадратичное отклонение
# функция gauss(mu, sigma)
g = random.gauss(0, 3.5)
print(g)

# функции мз модуля random для работы со списками
lst = [4, 5, 0, -1, 10, 76, 3]

# выбор одного элемента случайным образом
a = random.choice(lst)
print(a)

# shuffle - метод для перемешивания элементов в списке
random.shuffle(lst)
print(lst)

# выбор случайных неповторяющихся элементов (подпоследовательности)
# если указать количество элементов больше длины списка, будет ошибка
b = random.sample(lst, 3)
print(b)

# формирование одинаковой последовательности чисел при каждом запуске программы
# контроль генерации псевдо-случайных чисел
random.seed(123)
c = [random.randint(0, 10) for _ in range(20)]
print(c)

print("""
Задачи""")

# Task 2
# random.seed(1)
# a, b = map(int, input().split())
# print(a, b)
# c = a + (b-a) * random.random()
# print(round(c, 2))

# Task 3
# random.seed(1)
# a, b = map(int, input().split())
# print(random.randint(a, b))
# # Variant 2
# print(random.randint(*map(int, input().split())))

# Task 4
random.seed(1)
lst = ['Тула', 'Казань', 'Смоленск', 'Семипалатинск', 'Уфа', 'Москва', 'Самара']
# lst = input().split()
print(random.choice(lst))

# Task 5
import sys
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ["1 2 3 4", "5 6 7 8", "9 8 6 7"]
print(lst_in)
z1 = list(zip(*map(str.split, lst_in)))
print(z1)
random.shuffle(z1)
print(z1)
[print(*x) for x in zip(*z1)]
# z2 = zip(*z1)
# for x in z2:
#     print(*x)

# Task 6
lst = "Петров Иванов Сидоров Балакирев Фридман".split()
# lst = input().split()
random.seed(1)
print(*random.sample(lst, 3))

# Task 7
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = 10
# N = int(input())
P = [[0] * N for _ in range(N)]
print(*(x for x in P), sep='\n')


# Variant 1
def check_pos(lst, i, j):
    """Проверяет, что поля вокруг свободны"""
    n = len(lst) - 1
    i_top = i - 1 if i > 0 else i
    i_bot = i + 2 if i < n else i + 1
    j_left = j - 1 if j > 0 else j
    j_right = j + 2 if j < n else j + 1
    for x in lst[i_top:i_bot]:
        if any(x[j_left:j_right]):
            return False
    return True


M = 10
m_put = 0
while m_put < M:
    i = random.randint(0, N-1)
    j = random.randint(0, N-1)
    print(m_put, i, j)
    if check_pos(P, i, j):
        P[i][j] = 1
        m_put += 1
print(*(x for x in P), sep='\n')

# # Variant 2
# for _ in range(10):
#     while True:
#         r, c = random.randint(0, N - 1), random.randint(0, N - 1)
#         if not sum(P[i][y] for i in range(max(0, r - 1), min(r + 2, N))
#                            for y in range(max(0, c - 1), min(c + 2, N))):
#             P[r][c] = 1
#             break

