# 8.6 Обработка исключения FileNotFoundError и менеджер контекста

try:
    file = open("my_file.txt", encoding="utf-8")
    s = file.readlines()
    print(s)
    file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
