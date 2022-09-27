import pandas as pd #pandas untuk membuat dataframe
import openpyxl #openpyxl untuk interaksi antara python dan file excel

df = pd.read_excel('data_set/supermarket_sales.xlsx')

#select columns dan filter by gender
# df = df[['Gender', 'Customer type', 'Unit price', 'Quantity', 'Total']].loc[df['Gender'] == 'Female'].head()

#pivoting selection columns
df_pivot = df.pivot_table(index='Gender', columns='Payment', values='Total', aggfunc='sum').round(decimals=2)
print(f'Dataframe columns: {df.columns}')
print('Sample dataset:')
df = df_pivot.apply(pd.to_numeric, errors='coerce')
print(f'{df}')
print()

#save result to excel
# print('Save dataframe to excel.....')
# df_pivot.to_excel(excel_writer='data_set/report_2019.xlsx', sheet_name='Report Payment Method')
# df_pivot.to_csv(path_or_buf='data_set/report_2019.csv')
# print('Save dataframe done.....')

#save result to csv
print('Save dataframe to csv.....')
df_pivot.to_csv(path_or_buf='data_set/report_2019.csv')
print('Save dataframe done.....')