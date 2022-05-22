# 8.1 Импорт стандартных модулей. Команды import и from

import math
import time
import pprint
# по стандарту PEP-8 каждый модуль импортируется на отдельной строчке в начале программы


print(locals())

print("""
# Через модуль math, полный путь
""")
pprint.pprint(locals())

a = math.ceil(1.8)
print(a)
print(math.pi)

print("""
# Замена модуля на локальную переменную
""")
math = "математика"
pprint.pprint(locals())
# будет ошибка
# a = math.ceil(1.8)
# print(a)
# print(math.pi)


print("""
# Импорт модуля под псевдонимом
""")
import math as mt

pprint.pprint(locals())
a = mt.ceil(1.8)
print(a)
print(mt.pi)

print("""
# Импорт отдельных функций
""")
from math import ceil, pi

pprint.pprint(locals())
a = ceil(1.8)
print(a)
print(pi)


def ceil(x):
    print("\n", "# наша функция ceil", "\n")
    return x


a = ceil(1.8)
pprint.pprint(locals())
print(a)
print(pi)

print("""
# Импорт отдельных функций под псевдонимом
""")

from math import ceil as cl, pi

pprint.pprint(locals())
a = cl(1.8)
print(a)
print(pi)

# импорт всего содержимого библиотеке
# from math import *
# крайне не рекомендуется



