# 9.7 Аргумент key для сортировки по ключу

a = [4, 3, -10, 1, 7, 12]
b = sorted(a)
print(b)


def id_odd(x):
    return x % 2


# Добавляем ключ
a = [4, 3, -10, 1, 7, 12]
b = sorted(a, key=id_odd)
print(b)

b = sorted(a, key=lambda x: x % 2)
print(b)

# метод sort ведет себя аналогично
a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x % 2)


# более сложные правила сортировки
def key_sort(x):
    return x if x % 2 == 0 else 100 + x


a = [4, 3, -10, 1, 7, 12]
b = sorted(a, key=key_sort)
print(b)

lst = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]

# Сортировка по длине строки
b = sorted(lst, key=len)
print(b)

# Сортировка по последнему символу строки
b = sorted(lst, key=lambda x: x[-1])
print(b)

# Сортировка по первому символу строки
b = sorted(lst, key=lambda x: x[-1])
print(b)

books = (
    ("Евгений Онегин", "Пушкин А. С.", 200),
    ("Муму", "Тургенев И. С", 250),
    ("Мастер и Маргарита", "Булгаков М. А.", 500),
    ("Мертвые души", "Гоголь Н. В.", 190)
)

# Сортировка книг по цене
b = sorted(books, key=lambda x: x[-1])
print(b)

# Аргумент key используется для управления сортировкой элементов произвольных коллекций данных

print("""
Задачи
""")

# Task 1
# lst = input().split()
lst = 'Лена Енисей Волга Дон'.split()
print(*sorted(lst, key=len, reverse=True))

# Task 2
# Sample Input:
#
# ножницы=100
# котелок=500
# спички=20
# зажигалка=40
# зеркальце=50

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for s in lst_in:
#     k, v = s.split('=')
#     d[k] = int(v)
# print(*sorted(d, reverse=True, key=d.get))

# # Variant 2
# d = dict((c.split('=') for c in open(0)))
# print(*sorted(d, key=lambda x: int(d[x]), reverse=True))

# Variant 3
# d = {k: int(v) for k, v in (line.split('=') for line in lst_in)}
# print(*sorted(d, key=d.get, reverse=True))

# Task 3
scale = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

# phrase = input().split()
phrase = 'до до ре фа фа соль ля си'.split()
print(*sorted(phrase, key=scale.index))

# Task 4
lst_in = ["Номер;Имя;Оценка;Зачет",
          "1;Портос;5;Да",
          "2;Арамис;3;Да",
          "3;Атос;4;Да",
          "4;д'Артаньян;2;Нет",
          "5;Балакирев;1;Нет"
          ]

# import sys
#
# # считывание списка из входного потока (не меняйте переменную lst_in в программе)
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# Очень важно!
# Вложенные генераторы списков / кортежей !!
# Nested list comprehension / tuple comprehension !!!

# распрямление двумерного списка
# tp = tuple(int(x) if x.isnumeric() else x
#            for line in lst_in
#            for x in line.split(';')
#            )
# print(tp)

# операции с двумерным списком с сохранением структуры (без распрямления)
tp = tuple(tuple(int(x) if x.isnumeric() else x for x in line.split(';'))
           for line in lst_in)
print(tp)

seq_map = {0: 3, 1: 0, 2: 2, 3: 1}
t_sorted = tuple(tuple(sorted(line, key=lambda x: seq_map.get(line.index(x)))) for line in tp)
print(t_sorted)

# Task 5
lst_in = ['Атос=лейтенант',
          'Портос=прапорщик',
          "д'Артаньян=капитан",
          'Арамис=лейтенант',
          'Балакирев=рядовой']

sort_seq = 'рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник'
lst = list(map(lambda x: x.split('='), lst_in))
print(lst)
lst.sort(key=lambda x: sort_seq.find(x[1]))
print(lst)
