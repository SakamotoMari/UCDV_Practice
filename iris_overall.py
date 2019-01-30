# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import parallel_coordinates

# because the csv file does not include a header row, 
# we need to "manually" define the headers for our data 
# these headers are based on the information on 
# https://archive.ics.uci.edu/ml/datasets/Iris
header = ['sepal length','sepal width', 'petal length', 'petal width', 'class']
iris_df = pd.read_csv('iris.csv', encoding='utf-8', names=header)
# we could print the top of the DataFrame for sanity check
#print(iris_df.head())

#create parallel coordinates plot
plt.figure()
parallel_coordinates(iris_df, 'class')


# create one histograms per column the entire data set

## let's iterate over the column names:
#for dim in ['sepal length','sepal width', 'petal length', 'petal width']:
    # create a new figure
#    plt.figure()
    
    # let's plot the histogram, the bins argument is the resolution
#    iris_df[dim].plot.hist(bins=30)

    # let's label the horizontal axis
#    plt.xlabel(dim)

## create a scatter plot for the entire data set for each pair of columns
## let's iterate over the pairs of dimensions using two nested for loops
#for dim1 in ['sepal length','sepal width', 'petal length', 'petal width']:
#    for dim2 in ['sepal length','sepal width', 'petal length', 'petal width']:
#        # let's only plot if the dimensions are different
#        if dim1 != dim2:
            # lets' plot the scatter plot 
            # (note that in this case we do not need to create new figure
            # because the scatter function does that for us, it does feel
            # a bit arbitrary that some plot functions to and some don't)
#            iris_df.plot.scatter(x=dim1, y=dim2)
            # let's label the horizontal axis
#            plt.xlabel(dim1)
            # let's label the vertical axis
#            plt.ylabel(dim2)

# the next function shows all the figures we created, 
# and it waits untl we manually close all windows to 
# proceed (in this case to end the script)
plt.show()

