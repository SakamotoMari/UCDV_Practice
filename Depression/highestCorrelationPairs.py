import pandas as pd
import numpy as np 


df=pd.read_csv('hfi.csv',encoding='utf-8')

corr=df.corr()
#print("Correlation Matrix")
#print(corr)
#print()

corr_matrix=corr.abs()

c1=corr_matrix.unstack().sort_values().drop_duplicates()


print(c1[-50:])
