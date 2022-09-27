import pandas as pd
import numpy as np

# print(pd.__version__)
# print(np.__version__)

n_rows = 5
n_cols = 5

cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1,10, size=(n_rows, n_cols)), columns=cols)
# _prefix = df.add_prefix('Kolom_')
# _suffix = df.add_suffix('_field')
# print(_prefix)
# print(_suffix)