# 9.8 Функция isinstance для проверки типов данных

# Проверка на принадлежность объекта определенному типу данных

a = 5

print(isinstance(a, int))
print(isinstance(a, float))

b = True

# тип bool наследуется от типа int
print(isinstance(b, bool))
print(isinstance(b, int))

# строгая проверка - type
print(type(b) == bool)
print(type(b) == int)

# оператор 'is' соответствует оператору '=='
print(type(b) is bool)
print(type(b) is int)

print("""
# проверка соответствия нескольким типам данных """)
print(type(b) in (bool, float, str))

# отличия isinstance от type:
# isinstance осуществляет проверку с учетом иерархии наследования объектов
# isinstance была разработана для проверки принадлежности объекта тому или иному классу

# посчитать сумму только вещественных чисел в кортеже
data = (4.5, 8.7, True, "книга", 8, 10, -11, [True, False])

# вариант 1
s = 0
for x in data:
    if isinstance(x, float):
        s += x
print(s)

# вариант 2
# встроенные функции языка Python работают быстрее
s = sum(filter(lambda x: isinstance(x, float), data))
print(s)

# проверка на int
s = sum(filter(lambda x: type(x) is int, data))
print(s)

# множественные проверки
print(isinstance(a, (int, float)))
# это аналог
print(isinstance(a, int) or isinstance(a, float))

print("""
Задачи
""")


# Task 1
def get_add(a, b):
    if type(a) in (int, float) and type(b) in (int, float) or isinstance(a, str) and isinstance(b, str):
        return a + b
    # return None  # Функция по умолчанию возвращает None, есть не возвращает никакого другого значения


print(get_add(5, 10))
print(get_add('Привет, ', "Питон !"))
print(get_add(True, False))
print(get_add(10, 'Вася'))
print(get_add(2, '3'))
print(get_add('2', 3))
print(get_add(2.75, 0.25))
print(get_add(3.25, 10))

print(type('2'))

x = '2'
y = 3
print(type(x) and type(y) in (int, float))

# # Variant 2
# def get_add(a, b):
#     if {type(a), type(b)} in ({str}, {int}, {float}, {int, float}):
#         return a + b
#
# # Variant 3
# def get_add(a, b):
#     tset = {type(a), type(b)}
#     if tset <= {int, float} or tset == {str}:
#         return a + b


print("""
Task 3""")


# Task 3
def get_sum(it):
    s = 0
    for x in it:
        if type(x) == int:
            s += x
    return s


print(get_sum([1, 2, 3, "a", True, [4, 5], "c", (4, 5)]))
print(get_sum({5, 6, 7, '8', 5, '4'}))
print(get_sum((10, "f", '33', True, 12)))
print(get_sum(['1', True, False, (1, 23)]))

# # Variant 2
# def get_sum(it):
#     return sum(filter(lambda x: type(x) == int, it))


print("""
Task 4""")


# Task 4
def get_even_sum(it):
    return sum(filter(lambda x: type(x) == int and not x % 2, it))


print(get_even_sum([1, 2, 3, "a", True, [4, 5], "c", (4, 5)]))
print(get_even_sum({5, 6, 7, '8', 5, '4'}))
print(get_even_sum((10, "f", '33', True, 12)))
print(get_even_sum(['1', True, False, (1, 23)]))


print("""
Task 5""")


# Task 5
def get_list_dig(lst):
    return list(filter(lambda x: type(x) in (int, float), lst))


print(get_list_dig([1, 2, 3, "a", True, [4, 5], "c", (4, 5)]))
print(get_list_dig({5, 6, 7, '8', 5, '4'}))
print(get_list_dig((10, "f", '33', True, 12)))
print(get_list_dig(['1', 15.5, True, False, (1, 23)]))
