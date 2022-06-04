# Обход массива змейкой

a0 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(a0)


def move_snake(a, start, end):
    if start < end:
        res = []
        i = start
        for j in range(start, end):
            res.append(a[i][j])
        j = end
        for i in range(start, end):
            res.append(a[i][j])
        i = end
        for j in range(end, start, -1):
            res.append(a[i][j])
        j = start
        for i in range(end, start, -1):
            res.append(a[i][j])
        return res + move_snake(a, start + 1, end - 1)
    else:
        return []


a1 = move_snake(a0, 0, len(a0) - 1)
print(a1)


def move_snake2(a, start, end):
    if start < end:
        res = a[start][start:end] + [x[end] for x in a[start:end]] \
              + a[end][end:start:-1] + [x[start] for x in a[end:start:-1]]
        return res + move_snake2(a, start + 1, end - 1)
    else:
        return []


a2 = move_snake2(a0, 0, len(a0) - 1)
print(a2)


def move_snake3(a, start, end):
    if start < end:
        res = []
        for j in range(start, end):
            res.append(a[start][j])
        for i in range(start, end):
            res.append(a[i][end])
        for j in range(end, start, -1):
            res.append(a[end][j])
        for i in range(end, start, -1):
            res.append(a[i][start])
        return res + move_snake3(a, start + 1, end - 1)
    else:
        return []


a3 = move_snake3(a0, 0, len(a0) - 1)
print(a3)


def move_snake4(a, start, end):
    if start < end:
        return a[start][start:end] + [x[end] for x in a[start:end]] \
               + a[end][end:start:-1] + [x[start] for x in a[end:start:-1]] \
               + move_snake4(a, start + 1, end - 1)
    else:
        return []


a4 = move_snake4(a0, 0, len(a0) - 1)
print(a4)

