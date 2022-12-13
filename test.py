import pandas as pd
import numpy as np


df = pd.read_csv('attraction_info_final_1213.csv', encoding='utf-8')

# print(df.isnull().values.any())

# print(df.isna().values.any())

# print(df.columns)

df2 = df.replace({np.nan:None})

# print(df2.isna().values.any())

for i,row in df2.iterrows():
    print(row)