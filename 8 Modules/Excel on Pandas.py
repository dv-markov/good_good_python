import pandas as pd
import xlrd
import xlwt

# file_location = open('SAMSON/Vetec.xlsx')
file_location = 'E:\\_ARCHIVE\\YADISK\\Python\\Projects\\stepik1\\8 Modules\\SAMSON\\Vetec.xlsx'
# df = pd.read_excel(file_location)
df = pd.read_excel(io=file_location, index_col=0)
print(df)

# for index in df:
#     print(index)
#     for row in index:
#         print(row)

for index, row in df.iterrows():
    print('\n', index, len(row))
    print(row)


# rb = xlrd.open_workbook('SAMSON\\Vetec.xlsx', formatting_info=True)
# sheet = rb.sheet_by_index(0)
