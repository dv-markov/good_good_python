# 10.2 Битовые операции И, ИЛИ, НЕ, XOR

from time import time

a = 121
print(a, bin(a))

# битовое НЕ
# первый бит - знаковый
# битовое НЕ меняет значения всех битов числа на противоположные
b = ~a
print(b, bin(b))

d = 0
print(d, ~d)

d = 10
print(d, ~d)

d = -10
print(d, ~d)

# битовая операция И
# (побитовое И)
flags = 5  # 00000101
mask = 4   # 00000100
res = flags & mask
print(res)

# используется для проверки включен ли второй бит в переменной flags
if flags & mask == mask:
    print("Включен 2-й бит числа")
else:
    print("Второй бит числа выключен")

# битовое И используется также для выключения определенных бит числа
flags = 13  # 00001101
mask = 5    # 00000101
# flags = flags & ~mask
# альтернативная запись
flags &= ~mask
print(flags)  # 8  # 00001000

# битовая операция ИЛИ
# применяется, когда нужно включить отдельные биты переменной
flags = 8  # 00001000
mask = 5   # 00000101
# flags = flags | mask
# альтернативная запись
flags |= mask
print(flags)  # 13  # 00001101

# битовая операция XOR
# исключающее или
# с ее помощью удобно переключать биты
# единица в битая второго оператора переключает биты в первом
flags = 9
mask = 1
flags = flags ^ mask
print(flags)

# Операция XOR работает без потерь.
# При повторном применении возвращает исходное значение.
# Применяется, например, при шифровании, mask - это пароль
flags ^= mask
print(flags)

# приоритеты: ~, &, (| = ^)


# смещение бит вправо >>
# смещение бит влево <<
x = 160
print(x, bin(x))
# операция сдвига на бит вправо делит число на два
x = x >> 1
print(x, bin(x))
# сдвиг на два бита вправо делит число на 4
x = x >> 2
print(x, bin(x))


# при сдвиге числа с крайними единицами, правые значения теряются
x = x >> 2
print(x, bin(x))
# эквивалент целочисленного деления
x = x >> 1
print(x, bin(x))

# сдвиг влево эквивалентен умножению на 2 в соответствующей степени
x = x << 1
print(x, bin(x))
x = x << 3
print(x, bin(x))

# битовые сдвиги работают гораздо быстрее традиционного деления и умножения
# применяются для маломощных и встроенных систем


print("""
Задачи """)

# Task 2
a = 100
b = 8
print(a | b)
# print(int(input()) | 8)

# Task 3
a = 153
b = 18
print(a & ~b)
# print(int(input()) & ~18)

# Task 4
a = 58
b = 9
print(a ^ b)
# print(int(input()) ^ 9)

# Task 5
a = 40
b = 2
print(a << b)
# print(int(input()) << 2)

# Task 6
a = 22
b = 1
print(a >> b)
# print(int(input()) >> 1)

# Task 7
key = 123
# s1 = input()
s1 = 'ѩкю[щюлцхZ'
# res = (chr(ord(x) ^ key) for x in s1)
res = map(lambda x: chr(ord(x) ^ key), s1)
print(*res, sep='')

# Task 8
# Variant 1
# a = int(input())
a = 106
print("ДА" if a & 72 == 72 else "НЕТ")
print(bin(72))

# # Variant 2
# n = int(input())
# print(("ДА", "НЕТ")[n & (1 << 3) * n & (1 << 6) == 0])


# Task 9
def timer(funk, x):
    start = time()
    for i in range(1000000):
        funk(x)
    end = time()
    print("Время выполнения = ", end - start)


print(x & 2)
print(x & 32)
print(x & 128 or x & 32)

# Variant 1
# x = int(input())
x = 74
timer(lambda x: ("НЕТ", "ДА")[bool(x & 2 or x & 32)], x)
print(("НЕТ", "ДА")[bool(x & 2 or x & 32)])

# Variant 2
# x = int(input())
x = 74
timer(lambda x: ("НЕТ", "ДА")[x & 2 == 2 or x & 32 == 32], x)
print(("НЕТ", "ДА")[x & 2 == 2 or x & 32 == 32])

# Variant 3
timer(lambda x: "ДА" if x & 2 == 2 or x & 32 == 32 else "НЕТ", x)
print("ДА" if x & 2 == 2 or x & 32 == 32 else "НЕТ")

# Variant 4
timer(lambda x: "ДА" if x & 0b100010 else "НЕТ", x)
print("ДА" if x & 0b100010 else "НЕТ")

# Variant 5
timer(lambda x: "ДА" if x & 34 else "НЕТ", x)
print("ДА" if x & 34 else "НЕТ")


