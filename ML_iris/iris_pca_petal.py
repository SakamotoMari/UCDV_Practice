# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# because the csv file does not include a header row, 
# we need to "manually" define the headers for our data 
# these headers are based on the information on 
# https://archive.ics.uci.edu/ml/datasets/Iris
header = ['sepal length','sepal width', 'petal length', 'petal width', 'class']
iris_df = pd.read_csv('iris.csv', encoding='utf-8', names=header)
# we could print the top of the DataFrame for sanity check
#print(iris_df.head())

# let's extract the values of the two petal columns
# and store them in a new variable X
X = iris_df.loc[:,['petal length', 'petal width']].values

# lets create a PCA object
pca = PCA(n_components=2)
# let's project the data
projected = pca.fit_transform(X)

# the result of fig_transfor is a numpy array (just another data structure)
# let's convert it to a data frame
projected_df = pd.DataFrame(projected, columns=['proj1', 'proj2'])
# let's add the class column from the original dataframe to the new dataframe
projected_df['class'] = iris_df['class']

# we could print the top of the DataFrame for sanity check
#print(projected_df.head())

# scatter plot

# let's create a dictionary to define 
# what color we want for each type of iris
colours_dict = {
    'Iris-setosa': 'green',
    'Iris-virginica': 'blue',
    'Iris-versicolor': 'red'
}

# let's create a new figure, as above
fig, ax = plt.subplots()

by_class = projected_df.groupby('class')
# let's iterate again over the groups
for name, group in by_class:
    # let's plot a scatter using the two new dimensions
    dim1 = 'proj1'
    dim2 = 'proj2'
    # note again that we are calling the function with ax=ax 
    # to say that we want all plots to show up in the same figure 
    # we also specify what colour we want our data to be in 
    # and the label for it
    group.plot.scatter(x=dim1, y=dim2, 
                        label=name, c=colours_dict[name], ax=ax)
    # let's label the horizontal axis
    plt.xlabel(dim1)
    # let's label the vertical axis
    plt.ylabel(dim2)


# let's also plot the scatter plot over the petal dimensions for comparison
# let's create a new figure, as above
fig, ax = plt.subplots()

by_class = iris_df.groupby('class')
# let's iterate again over the groups
for name, group in by_class:
    dim1 = 'petal length'
    dim2 = 'petal width'

    group.plot.scatter(x=dim1, y=dim2, 
                        label=name, c=colours_dict[name], ax=ax)
    # let's label the horizontal axis
    plt.xlabel(dim1)
    # let's label the vertical axis
    plt.ylabel(dim2)


plt.show()
