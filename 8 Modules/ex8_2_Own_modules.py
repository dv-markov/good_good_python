# 8.2 Импорт собственных модулей
import sys

import folder.mymodule as mymodule

# import folder.mymodule
import pprint

pprint.pprint(sys.path)
print()

print(mymodule.NAME)
print("округление mymodule.floor(-5.4):", mymodule.floor(-5.4), "\n")

from folder.mymodule import floor

print("округление floor(-5.4):", floor(-5.4))
print("округление mymodule.math.floor(-5.4):", mymodule.math.floor(-5.4), "\n")

# длинную иерархию пространства имен обычно не используют
a = mymodule.math.floor(-5.4)
print("округление mymodule.math.floor(-5.4):", a, "\n")

print("округление mymodule.floor(-5.4):", mymodule.floor(-5.4))
print("округление mymodule.ceil(-5.4):", mymodule.ceil(-5.4), "\n")

pprint.pprint(sys.path)
print()

# Добавление директории модуля к системным путям проекта
# Такое решение используется крайне редко
# Обычно пусть указывается при импорте модуля
sys.path.append(r"E:\_ARCHIVE\YADISK\Python\Projects\stepik1\8 Modules\folder")
pprint.pprint(sys.path)
print()

# при импорте один раз выполняется весь код импортируемого модуля
