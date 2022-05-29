# 9.1 Выражения-генераторы

# кргулые скобки - чистый генератор
a = (x**2 for x in range(6))
print(a)

# генератор сам по себе является итератором
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# превышение диапазоны вызывает ошибку StopIteration
# print(next(a))

# перебрать элементы генератора можно только 1 раз
gen = (x**2 for x in range(6))
print("Первый вызов генератора gen")
for x in gen:
    print(x)
# если попытыться перебрать второй раз, результата не будет
print("Второй вызов генератора gen")
for x in gen:
    print(x)

# Функции, работающие с итераторами(генераторами):
# list, set, sum, max, min и другие
a1 = (x**2 for x in range(6))
print(list(a1))
a1 = (x**2 for x in range(6))
print(set(a1))
# Генератор можно перебрать только 1 раз
print(set(a1))
print(sum(x ** 2 for x in range(6)))
print(max(x ** 2 for x in range(6)))

# Генераторы, по сравнению с обычными списками, не хранят в памяти сразу все значения
# Они генерируют их по мере необходимости
# Пример - создание списка из триллиона значений невозможно сделать напрямую
# lst = list(range(1000000000000))
# создаем генератор списков такого размера
lst = (x for x in range(1000000000000))
for i in lst:
    print(i, end=" ")
    if i > 50:
        break
print()

# Функция len не работает от генератора
a = (x for x in range(10, 20))
# print(len(a))
# нужно сначала перевести генератор в список
b = list(a)
print(b)
print(len(b))

# при формировании списка генератором не стоит заключать его в скобки
print([(x ** 2 for x in range(10))])
# корректное формирование списка генератором
print([x ** 2 for x in range(10)])

# К генератору нельзя обращаться по индексу
z = (x for x in range(10))
# print(z[0])


print("""
# Задачи
""")


# Task 1
gen = (x for x in range(2, 10001))
print(gen)
# for x in gen:
#     print(x)

gen = range(2, 10001)
print(gen)
print()
# for x in gen:
#     print(x)

# Task 2
# ввод значений a и b (переменные a и b не менять!)
# a, b = map(int, input().split())
# gen = (x ** 2 for x in range(a, b + 1))
# tp = tuple(gen)
# print(tp)

# Task 3
# a, b = map(int, input().split())
# gen = (-x if x < 0 else x for x in range(a, b + 1))
# # # Version 1
# # for i, x in enumerate(gen):
# #     print(x)
# #     if i > 3:
# #         break
# # Version 2
# for i in range(5):
#     print(next(gen))

# Task 6
# a = int(input())
# gen1 = (abs(x) for x in range(-a, a + 1))
# gen2 = (x ** 3 for x in gen1)
# # Variant 1
# for i in range(4):
#     print(next(gen2), end=" ")
# # # Variant 2
# # print(*(next(gen2) for _ in range(4)))
# # # Variant 3
# # print(*(next(gen2) for i in '....'))

# Task 7
from string import ascii_lowercase
# print(ascii_lowercase)
gen = (char1 + char2 for char1 in ascii_lowercase for char2 in ascii_lowercase)
# print(gen)
for x in range(50):
    print(next(gen), end=" ")
print("\n")

# Task 8
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (cities[x % 6] for x in range(1000000))
print(*(next(gen) for i in range(20)))
print()

# Task 8
# a, b = map(int, input().split())
# gen = (0.5 * pow(x / 100, 2) - 2 for x in range(a * 100, b * 100 + 1))
# for x in range(20):
#     print(round(next(gen), 2), end=" ")
# print()

# test lst cycle with 2 entries
lst1 = [(1, '1a'), (2, '2a'), (3, '3a')]
print(lst1)
for k, v in lst1:
    print(k, v)


