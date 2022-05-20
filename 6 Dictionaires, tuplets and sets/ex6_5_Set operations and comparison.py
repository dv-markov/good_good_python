# 6.5 Операции над множествами. Сравнение множеств

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}

# Пересечение множеств
print("\n", "Пересечение множеств", sep='')
print(setA & setB)
setA &= setB
print(setA)
setA = {1, 2, 3, 4}
setC = {9, 10, 11}
print(setA & setC)
print(setA.intersection(setB))
print(setA.intersection_update(setB))
print(setA)

# Объединение множеств
print("\n", "Объединение множеств", sep='')
setA = {1, 2, 3, 4}
print(setA | setB)
setA |= setB
print(setA)
setA = {1, 2, 3, 4}
print(setA.union(setB))
print(setA)
print(setB)

# Вычитание множеств
print("\n", "Вычитание множеств", sep='')
print(setA - setB)
print(setB - setA)
setA -= setB
print(setA)

#  Симметричная разность множеств
print("\n", "Симметричная разность множеств", sep='')
setA = {1, 2, 3, 4}
print(setA)
print(setB)
print(setA ^ setB)

# Сравнение множеств
print("\n", "Сравнение множеств", sep='')
setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5, 6, 7}
print(setA == setB)
# множества равны, если их длина и элементы совпадают (порядок не учитывается)
print(setA != setB)

setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5}
print(setB < setA)
print(setB > setA)
setB.add(22)
print(setB < setA)
print(setB > setA)
setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5, 6, 7}
print(setA < setB)
print(setA <= setB)

# Задачи
print("\n", "Задачи", sep='')

# Task 1
# # Variant 1
# s1 = set(map(int, input().split()))
# s2 = set(map(int, input().split()))
# print(*sorted(s1 & s2))
# # Variant 2
# print(*sorted(set(input().split()) & set(input().split())))

# Task 2
# s1 = set(map(int, input().split()))
# s2 = set(map(int, input().split()))
# print(*sorted(s1 - s2))

# Task 3
# s1 = set(map(int, input().split()))
# s2 = set(map(int, input().split()))
# print(*sorted(s1 ^ s2))

# Task 4
# s1 = set(input().split())
# s2 = set(input().split())
# print(('НЕТ', 'ДА')[(s1 == s2)])

# Task 5
# marks = set(input().split())
# print('НЕ ДОПУЩЕН' if set('2') & marks else 'ДОПУЩЕН')

# Task 6
# setY1 = set(input().split())
# setY2 = set(input().split())
# print(('НЕТ', 'ДА')[(setY2 > setY1)])

# Task 7
# # Variant 1
# n = int(input())
# mpls = (1, 2, 3, 5, 7)
# set1 = {2, 3, 5}
# set2 = {x for x in mpls if n % x == 0}
# print(('НЕТ', 'ДА')[(set2 >= set1)])
# # Variant 2
# print('НЕТ' if int(input()) % 30 else 'ДА')
