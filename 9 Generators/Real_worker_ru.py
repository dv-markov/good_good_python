school = {'html': {'Ivan': 200, 'Petr': 100, 'Timofey': 50},
          'JS': {'Pro':
                     {'n1': 100,
                      'n2': 200},
                 'Standard':
                     {'m1': 10,
                      'm2': 20}
                 }
          }

print("Школа: ", school)


def dig(a):
    if type(a) != dict:
        global i
        i += 1
        return a
    summ = 0
    for x in a:
        summ += dig(a.get(x))
    return summ

i = 0
result = dig(school)
print(result)
print(i)




