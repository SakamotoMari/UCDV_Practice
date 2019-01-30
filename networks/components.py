# -*- coding: utf-8 -*-
import pandas as pd
from scipy.sparse.csgraph import connected_components
from scipy import sparse
import numpy as np


# load the collaboration data, use the first row as header and the first column as index
collaborations_df = pd.read_csv('selected.csv', encoding='utf-8', header=0, index_col=0)

# create an empty list to store the rows as lists
all_rows = []

# iterate over the dataframe rows
for name1 in collaborations_df.index:
        # get the row from the index
        row = collaborations_df.loc[name1]
        # print for sanity check
        # print(row)
        # conver the row to list and append it to the list we created earlier
        all_rows.append(row.tolist())

# at this point all_rows should contain all the rows of the dataframe, each 
# stored as a list

# we can create a coo_matrix with this list of lists
# we need to tell the library that the data is of type np.uint8
matrix = sparse.coo_matrix(all_rows, dtype=np.uint8)

# sanity check printing
#print('matrix')
#print(matrix.toarray())

# now we can call the function to calculate the connected components
n_components, labels = connected_components(matrix, directed=False)

# sanity check printing
#print('n_components:', n_components)
#print('len(labels):', len(labels))
#print('labels:', labels)
#print('names:', collaborations_df.index)
#print()

# we can add the labels as a new column to the dataframe
collaborations_df['group'] = labels

# sanity check printing
#print(collaborations_df)

# we also need to add the labels as a ne row, but this can be done 
# by copy&paste in excel (usign paste special with the transpose option)

# save to file the dataframe with the added column
collaborations_df.to_csv('labelled.csv')