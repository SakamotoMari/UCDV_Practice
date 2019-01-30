from scipy import sparse
from scipy.sparse.csgraph import connected_components
import pandas as pd
import numpy as np

#read the csv file
dtsource=pd.read_csv('selected.csv', encoding= 'utf-8', header=0, index_col=0)
#turn the rows into lists
# failure!! refer to 'components.py' to see the correct example
dtlist = dtsource.values.tolist()
#print(dtlist[0])
spsmtx = sparse.coo_matrix(dtlist, dtype=np.uint8)

#get a list of labels representing the connected components
n_components, labels = connected_components(spsmtx, directed=False)
#print(n_components)
#print(labels)

dtsource['labels'] = labels
#print(dtsource)

dtsource.to_csv('cntcmp.csv')