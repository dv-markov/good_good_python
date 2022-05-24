import pandas as pd

df = pd.read_excel('E:\\_ARCHIVE\\YADISK\\Python\\Projects\\stepik1\\8 Modules\\SAMSON\\Vetec.xlsx')

print(df.head())

df['Left+Sold'] = df['Left on stock'] + df['Sold']
df['Check'] = df['Left+Sold'] - df['Purchased']

print(df.head())


def double_num(num):
    return num * 2


df['Doubled'] = df['Left+Sold'].apply(double_num)
print(df.head())

print(df)
d = dict()

# writer = pd.ExcelWriter('new_Vetec.xlsx')
# df.to_excel(writer, 'new_sheet')
# writer.save()
