import pandas as pd
from matplotlib import pyplot as plt
from sklearn import neighbors


header = ['sepal length','sepal width', 'petal length', 'petal width', 'class']
iris_df = pd.read_csv('iris.csv', encoding='utf-8', names=header)

#pd.plotting.scatter_matrix(
#   iris_df[['sepal length','sepal width', 'petal length', 'petal width']]) 


colours_list = []
for c  in iris_df['class']:
    if c == 'Iris-setosa':
        colours_list.append('green')
    elif c == 'Iris-virginica': 
        colours_list.append('blue')
    elif 'Iris-versicolor':
        colours_list.append('red')
    else:
        print('unexpected class!')

#pd.plotting.scatter_matrix(
#    iris_df[['sepal length','sepal width', 'petal length', 'petal width']], 
#    color=colours_list)

#plt.show()

#split the dataset into training part and testing part
#method 1
#training = iris_df.sample(frac=0.8)
#testing = iris_df.loc[~iris_df.index.isin(training.index)]

#method 2: randomly
by_class = iris_df.groupby('class')

# let's create two lists to store the training and testing subsets of each class
training_list = []
testing_list = []

# we now iterate by class
for name, group in by_class:
    training = group.sample(frac=.8)
    # get the remaining rows
    # based on: https://stackoverflow.com/a/32606673/6872193
    testing = group.loc[~group.index.isin(training.index)]

    # append to the lists
    training_list.append(training)
    testing_list.append(testing)

# create two new dataframes from the lists
training = pd.concat(training_list)
testing = pd.concat(testing_list)

#linewidth: training=0, tesing=1
#linewidth_list = []
#for w  in iris_df['class']:
#    if #:
#        linewidth_list.append(0)
#    elif #: 
#        linewidth_list.append(1)
#    else:
#        print('unexpected class!')


#pd.plotting.scatter_matrix(
#    iris_df[['sepal length','sepal width', 'petal length', 'petal width']], 
#    c=colours_list,
#    linewidths=linewidth_list,
#    edgecolors='black')

clf=neighbors.KNeighborsClassifier(15)

features = ['sepal length','sepal width', 'petal length', 'petal width']
training_matrix = training[features].values
training_labels = training['class'].values

clf = clf.fit(training_matrix, training_labels)

predicted = clf.predict(testing[features].values)

# the following might be a little tricky to read at first
# what we are doing here is creating a new variable named 'incorrect'
# and we are assigning to it a list of True/False values resulting from 
# the operation predicted != testing['class'] 
incorrect = predicted != testing['class']
# similar to the line above..
correct = predicted == testing['class']
# with the sum function, True counts as 1, and False as 0
accuracy = sum(correct)/len(testing)*100
print(sum(incorrect), 'incorrect classifications i.e.', accuracy, "% correct")