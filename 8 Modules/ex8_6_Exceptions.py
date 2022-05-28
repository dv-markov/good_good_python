# 8.6 Обработка исключения FileNotFoundError и менеджер контекста

# критический код
try:
    file = open("my_file.txt", encoding="utf-8")
    try:
        s = file.readlines()
        # int(s)  # вызывает ошибку при работе с файлом
        print(s)
    finally:
        file.close()
# обработка исключения
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")

# выполняется в любом случае, произошли ошибки или нет
# finally

# вариант 2 - менеджер контекста
# замена try/finally
# автоматически закрывает файл
try:
    with open("my_file.txt", encoding="utf-8") as file:
        s = file.readlines()
        # int(s)
        print(s)
except FileNotFoundError:
    print("Невозможно открыть файл")
except Exception:
    print("Ошибка при работе с файлом")
finally:
    print(file.closed)


print("""
# Задачи
""")

# Task 2
try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")
