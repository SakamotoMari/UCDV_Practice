# coding:utf-8

import pandas as pd
import sys

# we load the data into a dataframe
collaborations_df = pd.read_csv('selected.csv', encoding='utf-8', header=0, index_col=0)

# the first thing we need to write is this:
initial_sting = "graph {"
# so we print it out 
print(initial_sting)

# iterate over the rows of the dataframe:
for name1 in collaborations_df.index:
    # get the actual row data
    row = collaborations_df.loc[name1]

    # comparing the row values with zero produces
    # a list of True/False values 
    # (True where the item is > 0, False otherwise)
    non_zero_positions = row > 0
    # we can use this list to select items of the index
    # corresponding to values > 0
    coauthors = collaborations_df.index[non_zero_positions]
    
    # now the coauthors variable contains the names of the coauthors
    # of the author in the current row (i.e. the coauthors of name1)
    
    # let's iterate over the co-authors:
    for name2 in coauthors:
        # We want to express that there is a link between name1 and name2.
        # However, we want to avoid the case where name1 and name2 
        # are the same, and we also want to express each link only one time.
        # For example we want to express: Ann -- Yvonne, but not Yvonne -- Ann
        # To address this, we can use a "trick": comparing two strings in python
        # with '<' returns True only if the first string comes alphabetically 
        # before the second string
        # For example, the following will be executed only when 
        # name1 is Ann and name2 is Yvonne, but not when name1 is Ann and 
        # name2 is Yvonne (because Ann < Yvonne):
        if name1 < name2:
            # to express the link between two nodes in graphviz
            # we need to write:
            # 'name1 -- name2;'
            # however, if the names contain spaces (and in our case they do)
            # we need to wrap the names in quotes
            # to do that we can use '+' to join strings together as follows:
            print('"' + name1 + '" -- "' + name2 + '";')
            # another way to combine strings is to use the % notation
            #print('"%s" -- "%s";' % (name1, name2))

# after we iterate over all rows, we need to "close" the graph
final_string = "}"
# so we print it out 
print(final_string)

