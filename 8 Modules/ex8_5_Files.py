# 8.5 Функция open. Чтение данных из файла

# файл в папке с исполняемым
# относительный путь
open("my_file.txt")
# абсолютный путь
open(r"E:/_ARCHIVE/YADISK/Python/Projects/stepik1/8 Modules/my_file.txt")

# файл в подкаталоге в исполняемым
# относительный путь
open("images/img.txt")
# абсолютный
open(r"E:/_ARCHIVE/YADISK/Python/Projects/stepik1/8 Modules/images/img.txt")

# внешний файл
open("../out.txt")
open("../Ext/prt.dat")
open(r"E:/_ARCHIVE/YADISK/Python/Projects/stepik1/Ext/prt.dat")

file = open("my_file.txt")

