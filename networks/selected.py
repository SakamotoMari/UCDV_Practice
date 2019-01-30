# -*- coding: utf-8 -*-
import pandas as pd

#read csv files
df_mtx=pd.read_csv('matrix.csv', encoding='utf-8', header=0, index_col=0)
df_name=pd.read_csv('names.csv', encoding='utf-8', names=['name'])
#print(df_mtx)
#print(df_name)

#turn the dataframe of name into a list of names
list_name=df_name['name'].tolist()

#create a blank dataframe
cnt_name=len(df_name.index)
#print(cnt_name)
df_s=pd.DataFrame(0, index=list_name, columns=list_name)
#print(df_s)

#select the matching names from the matrix
for dim1 in list_name:
    if dim1 in df_mtx:
        for dim2 in list_name: 
            if dim2 in df_mtx: #the matrix is symmetrical, so I can directly use 'if in' to check if dim exists
                df_s.loc[dim2, dim1] = df_mtx.loc[dim2, dim1]

#print(df_s)
#print csv file
df_s.to_csv('selected.csv')

