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