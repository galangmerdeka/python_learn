import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5

cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1,5, size=(n_rows, n_cols)), columns=cols)

#membalik urutan kolom
print(df.loc[:, ::-1])
print()

#membalik urutan baris
print(df.loc[::-1])
print()

#membalik urutan baris dan penyesuaian ulang index
print(df.loc[::-1].reset_index(drop=True))