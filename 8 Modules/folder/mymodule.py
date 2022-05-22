import math
# from .. import ex8_2_Own_modules

# импортировать все содержимое модуля крайне не рекомендуется
# from math import *

from math import pi, ceil

NAME = "mymodule"


def floor(x):
    print("функция floor из модуля mymodule")
    return x


if __name__ == "__main__":
    for i in range(5):
        print(NAME)

