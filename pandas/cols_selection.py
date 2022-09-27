import pandas as pd
import numpy as np
import pandas.util.testing as pdus

n_rows = 5
n_cols = 2

cols = ['bil_pecahan', 'bil_bulat']

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), columns=cols)

df['bil_pecahan'] = df['bil_pecahan'].astype('float')

df.index = pdus.makeDateIndex(n_rows, freq='H') #untuk generate date time sbg index
df = df.reset_index()

df['teks'] = list('ABCDE')

# print(df.dtypes)

#hanya menampilkan kolom data yang bertipe numeric saja.
# print(df.select_dtypes(include='number'))

#hanya menampilkan kolom data yang bertipe float saja.
# print(df.select_dtypes(include='float'))

#hanya menampilkan kolom data yang bertipe int saja.
# print(df.select_dtypes(include='int'))

#hanya menampilkan kolom data yang bertipe string/object saja.
# print(df.select_dtypes(include='object'))

#hanya menampilkan kolom data yang bertipe datetime saja.
# print(df.select_dtypes(include='datetime'))

#hanya menampilkan kolom data yang bertipe object dan numeric.
print(df.select_dtypes(include=['object','number']))