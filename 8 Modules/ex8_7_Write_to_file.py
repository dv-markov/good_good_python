# 8.7 Запись данных в файл

file = open("out.txt", "w")
file.write("Hello World!")
file.close()

# try/except и менеджер контекста with обязательны при работе с файлами
try:
    with open("new_folder/out1.txt", "w") as file:
        file.write("Hello1")
        file.write("Hello2")
        file.write("Hello3")
except:
    print("Ошибка при работе с файлом")

try:
    with open("new_folder/out2.txt", "w") as file:
        file.write("Hello1\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
except:
    print("Ошибка при работе с файлом")
