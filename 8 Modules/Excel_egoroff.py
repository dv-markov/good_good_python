import openpyxl

book = openpyxl.open('new_Vetec.xlsx', read_only=True)
sheet = book.active

print(sheet["B2"].value)
print(sheet[1][2].value)

# работа с рядами и колонками
for row in range(1, sheet.max_row + 1):
    # print(sheet[row])
    offer = sheet[row][3].value
    AB = sheet[row][4].value
    pos = sheet[row][5].value
    print(row, offer, AB, pos)

# работа с диапазонами
cells = sheet['B1':'D11']
for pos, stor, offer in cells:
    print(pos.value, stor.value, offer.value)

# iterrows
for row in sheet.iter_rows(min_row=2, max_row=20, min_col=1, max_col=13):
    for cell in row:
        print(cell.value, end=' ')
    print()

sheet_2 = book.worksheets[0]
print(sheet_2)



book.close()


