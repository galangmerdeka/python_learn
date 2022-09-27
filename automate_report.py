import pandas as pd #pandas untuk membuat dataframe
import openpyxl as px #openpyxl untuk interaksi antara python dan file excel

df = pd.read_excel('data_set/supermarket_sales.xlsx')
print(df)