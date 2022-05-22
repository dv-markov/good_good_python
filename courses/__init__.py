# абсолютный импорт
# from courses.python import get_python

# варианты импорта в файл __init__.py
# нужно указывать абсолютный или относительный путь
# import courses.java
# from courses.java import *
# from .java import *

# относительный импорт
# только через from
from .python import get_python
from . import html, java

# внутри пакетов допустимо делать импорт всего содержимого модуля
from .php import *
from .doc import *

NAME = "package courses"


