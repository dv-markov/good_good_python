school = {0: {0: 200, 1: 100, 2: 50},
          1: {0:
                  {0: 100,
                   1: 200},
              1:
                  {0: 10,
                   1: 20}
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
