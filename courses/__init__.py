# абсолютный импорт
# from courses.python import get_python

# import java
# from java import *
# # from .java import *
# # import .panda
#
# from courses.java import *
# import courses.java

# относительный импорт
# только через from
from .python import get_python
from . import html, java

# внутри пакетов допустимо делать импорт всего содержимого модуля
from .php import *
from .doc import *

NAME = "package courses"


