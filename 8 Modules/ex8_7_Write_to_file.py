# 8.7 Запись данных в файл

import pickle

file = open("out.txt", "w")
file.write("Hello World!")
file.close()

# try/except и менеджер контекста with обязательны при работе с файлами
# открытие файла на запись
try:
    with open("new_folder/out1.txt", "w") as file:
        file.write("Hello1")
        file.write("Hello2")
        file.write("Hello3")
except:
    print("Ошибка при работе с файлом")

# открытие файла на дозапись (append)
try:
    with open("new_folder/out2.txt", "a") as file:
        file.write("Hello1\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
        # чтение файла в этом режиме невозможно
        # s = file.readlines()
except:
    print("Ошибка при работе с файлом")

# режим одновременного добавления и чтения данных
try:
    with open("new_folder/out2.txt", "a+") as file:
        # файловая позиция в режиме "а+" указывает на конец файла
        # поэтому файловую позицию на чтение надо переместить в начало
        file.seek(0)
        # файловые позиции на запись и чтение отличаются
        file.write("Hello4\n")
        file.writelines(["Hello5\n", "Hello6\n"])
        s = file.readlines()
        # считываются только те данные, которые были записаны в файл ранее
        print(s)

except:
    print("Ошибка при работе с файлом")

# бинарный режим доступа
books = [
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.С.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500),
    ("Мертвые души", "Гоголь Н.В.", 190)
]

try:
    with open("new_folder/out3.bin", "wb") as file:
        pickle.dump(books, file)
except Exception:
    print("Ошибка при работе с файлом")

try:
    with open("new_folder/out3.bin", "rb") as file:
        bs = pickle.load(file)
except Exception:
    print("Ошибка при работе с файлом")

print(bs)

# сохранение значений нескольких переменных в бинарный файл
book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
book2 = ["Муму", "Тургенев И.С.", 250]
book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
book4 = ["Мертвые души", "Гоголь Н.В.", 190]

try:
    with open("new_folder/out4.bin", "wb") as file:
        pickle.dump(book1, file)
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)
except Exception:
    print("Ошибка при работе с файлом")

try:
    with open("new_folder/out4.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except Exception:
    print("Ошибка при работе с файлом")

print(b1, b2, b3, b4, sep="\n")
