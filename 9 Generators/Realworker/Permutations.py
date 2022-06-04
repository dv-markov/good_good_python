lst0 = ['a', 'b', 'c', 'd']


def get_permutations(*args, lst):
    if len(lst) < 2:
        return [list(args) + lst]
    else:
        res = []
        for i, x in enumerate(lst):
            res += get_permutations(*args, x, lst=lst[:i] + lst[i + 1:])
        return res


lst1 = get_permutations(lst=lst0)
print(len(lst1))
for k in lst1:
    print(k)

R = 8
lst2 = get_permutations(lst=list(range(R)))
print(len(lst2))

try:
    with open('perm_result_2.txt', 'w') as file:
        file.write("Перестановки массива: " + str(list(range(R))) + '\n')
        file.write("Количество перестановок: " + str(len(lst2)) + '\n')
        for x in lst2:
            file.write(str(x) + '\n')
        print("Файл успешно записан")
except:
    print("Ошибка при работе с файлом")
