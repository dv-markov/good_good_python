# 3.8 Методы списков

a = [1, -54, 3, 23, 43, -45, 0]
print(a)

# добавление элемента в конец
print("\n", "Append ", sep='')
a.append(100)
print(a)
# Методы изменяют сам список и возвращают значение None
a = a.append(100)
print(a)

a = [1, -54, 3, 23, 43, -45, 0]
a.append(True)
print(a)

a.append([1, 2, 3])
print(a)

# Добавление элемента в произвольную позицию списка
print("\n", "Insert ", sep='')
a.insert(3, -1000)
print(a)

# Удаление элементов
# remove удаляет первое найденное значение
# булево значение при поиске приравнивается к числовому
print("\n", "Remove ", sep='')
a.remove(True)
print(a)
a.remove(True)
print(a)
# Несуществующие значение удалить нельзя

# Метод pop
# Без аргументов удаляет последний элемент.
# Возвращает значение удаленного элемента
print("\n", "Pop ", sep='')
print(a.pop())
print(a)
end = a.pop()
print(end)
print(a)
# также удалить можно любой элемент по индексу
a.pop(3)
print(a)

# очистка списка
a.clear()

a = [1, -54, 3, 23, 43, -45, 0]

# копирование списка
# все указанные способы дают идентичный результат, чаще всего используется срез
print("\n", "Копирование списка ", sep='')
c = a.copy()
print(id(a))
print(id(c))
d = a[:]
e = list(a)
print(id(d))
print(id(e))

# подсчет количества элементов в списке
print("\n", "Count ", c, sep='')
print(c.count(1))
c.append(1)
print(c.count(1))
print(c.count(True))
print(c.count('sdf'))

print("\n", "Index ", c, sep='')
print(c.index(1))
print(c.index(-54))
# Можно задать стартовый индекс
print(c.index(1, 2))
# перед поиском лучше проверить наличие элемента
print("asdf" in c)
# print(c.index("asdf"))

# инверсия порядка элементов в списке
print("\n", "Reverse ", sep='')
c.reverse()
print(c)

# Сортировка списка
# По умолчанию - сортировка по неубыванию
print("\n", "Sort ", sep='')
c.sort()
print(c)
c.sort(reverse=True)
print(c)
lst = ["Москва", "Санкт-Петербург", "Тверь", "Казань"]
print(lst)
lst.sort()
print(lst)

# Задачи
print("\n", "Tasks", sep='')

# # Task 2
# lst = list(map(int, input().split()))
# lst.append(lst[0] != lst[-1])
# print(*lst)

# Task 4
# # Variant 1
# lst = list(input())
# del lst[0]
# lst[0] = "8"
# lst.remove("-")
# lst.remove("-")
# print("".join(lst))
# # Variant 2
# lst = input()
# lst = lst.replace("-", "")
# lst = list(lst)
# del lst[0]
# lst[0] = "8"
# print("".join(lst))
# # Variant 3
# lst = list(input().replace("+7", "8").replace("-", ""))
# print("".join(lst))

# Task 5
# # Variant 1
# fio = input().split()
# print(fio)
# print("".join([fio[2], " ", fio[0][0], ".", fio[1][0], "."]))
# # Variant 2
# fio = input().split()
# print(f"{fio[2]} {fio[0][0]}.{fio[1][0]}.")

# Task 7
# # Variant 1
# l1 = list(map(int, input().split()))
# l2 = [l1.pop(l1.index(min(l1))), l1.pop(l1.index(min(l1))), l1.pop(l1.index(min(l1)))]
# print(*l2)
# # Variant 2
# lst = list(map(int, input().split()))
# print(*sorted(lst)[0:3])

# # Task 8
# lst = list(map(int, input().split()))
# lst[-1] = lst[-1] % 2 == 1
# print(*lst)

# Task 10
# Подвиг 10. Вводятся названия рек в одну строчку через пробел.
# Необходимо все их отсортировать по именам (по возрастанию) и в отсортированном списке удалить первый элемент.
# Результат отобразить на экране в одну строчку через пробел.
# # Variant 1
# lst = input().split()
# lst.sort()
# lst.pop(0)
# print(*lst)
# # Variant 2
# lst = input().split()
# print(*sorted(lst)[1:])

# test labs
# Удаление элементов списка
print(d)
del d[:3]
print(d)
d[0:2] = []
print(d)
print(e)
del e[::2]
print(e)
e.remove(23)
print(e)
