school = [0, 1, 2, 3, [10, 12, [1, 2, 3, 4, 5]], 11]
# print("Школа: ", school)


def dig(a):
    return len(a) + sum([dig(x) for x in a]) if type(a) == list else 0
    

print(dig(school))
