import pprint
import sys

sys.path.append(r"E:\_ARCHIVE\YADISK\Python\Projects\stepik1\8 Modules")
import mymodule1


# pprint.pprint(sys.path)
print("ex1")

# модуль при импорте выполняется только 1 раз
# даже если импорт прописан два раза или указан в перекрестных ссылках из другого модуля

# для повторного импорта используется importlib
import importlib
importlib.reload(mymodule1)
