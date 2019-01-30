# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt

# because the csv file does not include a header row, 
# we need to "manually" define the headers for our data 
# these headers are based on the information on 
# https://archive.ics.uci.edu/ml/datasets/Iris
header = ['sepal length','sepal width', 'petal length', 'petal width', 'class']
iris_df = pd.read_csv('iris.csv', encoding='utf-8', names=header)
# we could print the top of the DataFrame for sanity check
#print(iris_df.head())

# let's group by the values in the class column
by_class = iris_df.groupby('class')

# let's iterate over the column names:
for dim in ['sepal length','sepal width', 'petal length', 'petal width']:
    # create a new figure, this time using a different 
    # function, because we need the ax object that this 
    # function returns -- how would we know we need to 
    # use this? Generally from examples we find on the web
    fig, ax = plt.subplots()

    # lets' iterate over the groups created with groupby
    # for more information about this operation see:
    # https://pandas.pydata.org/pandas-docs/stable/groupby.html#iterating-through-groups 
    for name, group in by_class:
        # name is the group name
        # group is a dataframe with the group data
        # let's plot a histogram of the dim column of the current group
        # note that we are labelling the histogram with the group name
        # and we are passing the ax object to tell the function that 
        # we want this histogram to show in the existing figure with 
        # the other histograms, rather than in a new figure by its own
        group[dim].plot.hist(bins=30, label=name, ax=ax)

    # let's label the horizontal axis
    plt.xlabel(dim)

    # now, unfortunately we need a bit of a hack to display the legend
    # (there might be a better way of achieving this, sorry!)
    # lets' get the elements of the legend
    # for reference: https://matplotlib.org/1.3.1/users/legend_guide.html
    patches, labels = ax.get_legend_handles_labels()
    # let's create a list of labels, based on the group names
    # my notes: x[0] refers to the name 'class', by which the original data is divided. 
    # Necessary to check the data structure of 'groupby' for better understanding!
    new_labels = [x[0] for x in by_class]
    # let's keep only the last 3 patches and ignore the rest
    ## why???
    patches = patches[-3:]
    # let's update the figure legend with the lists we created/updated
    ax.legend(patches, new_labels, loc='best')

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
# let's iterate again over the groups
for name, group in by_class:
    # this time for simplicity we plot just one 
    # scatter plot, petal length vs petal width
    dim1 = 'petal length'
    dim2 = 'petal width'
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

# Data manipulation

# subtract the corresponding mean value
by_class.transform(lambda x:x-x.mean())

#clcopy=iris_df['class'].copy()
#for indices in by_class.groups.values():
#    iris_df.loc[indices] -= iris_df.loc[indices].mean()
#iris_df['class']=clcopy

#new scatter plot
fig, ax = plt.subplots()
for name,group in by_class:
    dim1 = 'petal length'
    dim2 = 'petal width'
  
    group.plot.scatter(x=dim1, y=dim2, 
                        label=name, c=colours_dict[name], ax=ax)
    # let's label the horizontal axis
    plt.xlabel(dim1)
    # let's label the vertical axis
    plt.ylabel(dim2)

#scale by MAX
by_class.transform(lambda x: x/x.max())

#clcopy=iris_df['class'].copy()
#for indices in by_class.groups.values():
#    iris_df.loc[indices] /= iris_df.loc[indices].max()
#iris_df['class']=clcopy

by_class = iris_df.groupby('class')
#new scatter plot
fig, ax = plt.subplots()
for name,group in by_class:
    dim1 = 'petal length'
    dim2 = 'petal width'

    group.plot.scatter(x=dim1, y=dim2, 
                        label=name, c=colours_dict[name], ax=ax)
    # let's label the horizontal axis
    plt.xlabel(dim1)
    # let's label the vertical axis
    plt.ylabel(dim2)



# the next function shows all the figures we created, 
# and it waits untl we manually close all windows to 
# proceed (in this case to end the script)
plt.show()
