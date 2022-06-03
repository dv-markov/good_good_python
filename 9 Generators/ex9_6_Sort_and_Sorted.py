# 9.6 Сортировка с помощью sort и sorted

a = [4, 3, -10, 1, 7, 12.5]
# метод sort ничего не возвращает
a.sort()
print(a)

b = [4, 3, -10, 1, 7, 12.5, "abc"]
# метод sort вернет ошибку
# a.sort()

a = [4, 3, -10, 1, 7, 12.5]
a.sort(reverse=True)
print(a)

# Функция sorted
a = [4, 3, -10, 1, 7, 12.5]
print(sorted(a))
print(sorted(a, reverse=True))

# Сортировка кортежей
r = ("Волга", "Лена", "Дон", "Енисей")
print(sorted(r))

# сортировка строки
print(sorted("python"))

# сортировка словарей
d = {"river": "река", "house": "дом", "tree": "дерево", "road": "дорога"}
# по умолчанию - сортировка ключей
print(sorted(d))
# сортировка значений
print(sorted(d.values()))
# сортировка пар ключ-значение
print(sorted(d.items()))
# сортировка словаря по ключам
print(dict(sorted(d.items())))

print("""
Задачи
""")

# Task 2
# s = input()
s = '-2 -1 8 11 4 5 '
lst = list(map(int, s.split()))
tp_lst = tuple(lst)
lst.sort()
tp_lst = tuple(sorted(tp_lst))
print(lst)
print(tp_lst)

# Task 3
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# Variant 1
def get_sort(d):
    return [v for k, v in sorted(d.items(), reverse=True)]
print(get_sort(d))
# Variant 2
def get_sort2 (d):
    return [d[i] for i in sorted(d, reverse=True)]
print(get_sort2(d))

# Task 4
# s = set(map(int, input().split()))
lst_in = '10 5 4 -3 2 0 5 10 3'
s = set(map(int, lst_in.split()))
print(*sorted(s, reverse=True)[:4])

