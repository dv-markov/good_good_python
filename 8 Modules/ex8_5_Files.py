# 8.5 Функция open. Чтение данных из файла

# # файл в папке с исполняемым
# # относительный путь
# open("my_file.txt")
# # абсолютный путь
# open(r"E:/_ARCHIVE/YADISK/Python/Projects/stepik1/8 Modules/my_file.txt")
#
# # файл в подкаталоге в исполняемым
# # относительный путь
# open("images/img.txt")
# # абсолютный
# open(r"E:/_ARCHIVE/YADISK/Python/Projects/stepik1/8 Modules/images/img.txt")
#
# # внешний файл
# open("../out.txt")
# open("../Ext/prt.dat")
# open(r"E:/_ARCHIVE/YADISK/Python/Projects/stepik1/Ext/prt.dat")

file = open("my_file.txt", encoding='utf-8')
print(file.read(4))
print(file.read(4))

# управление файловой позицией
file.seek(0)
print(file.read(4))
pos = file.tell()
print(pos)
# русские файлы - два байта на символ
print(file.readline(), end="") # \n
print(file.readline())

# печать всего файла построчно через цикл
file.seek(0)
for line in file:
    print(line, end="")

# прочитать все строки
file.seek(0)
s = file.readlines()
print('\n', s, sep='')

file.close()

