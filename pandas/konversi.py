import pandas as pd

data = {'col1': ['1','2','3','teks'],
        'col2': ['1','2','3','4']}

df = pd.DataFrame(data)

#konversi data pada kolom 2 ke numerik float
#method astype() berguna jika hanya 1 kolom yang dikonversi
# df_cols2 = df.astype({'col2':'float'})

#konversi tipe data ke numeric dengan to_numeric
#berguna untuk multiple columns
#value 'coerce' adalah jika dalam suata terdapat value yg tidak dapat dikonversi ke numerik maka akan di return sebagai NaN
df_all = df.apply(pd.to_numeric, errors='coerce')

print(df_all)