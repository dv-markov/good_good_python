# 8.3 Установка сторонних модулей. Пакетная установка

import sys

# перечень установленных пакетов
# pip list

# Обновления
# pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

# pip help
# pip install ...
# pip uninstall ...

print(sys.path)

# создание файла для пакетной установки
# pip freeze > requirements.txt

# установка пакета модулей из файла:
# pip install -r requirements.txt

