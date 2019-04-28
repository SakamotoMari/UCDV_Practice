# coding:utf-8

import pandas as pd
import sys

# we load the data into a dataframe
collaborations_df = pd.read_csv('MaayaCollaboration.csv', encoding='utf-8', header=0)

# the first thing we need to write is this:
initial_sting = "digraph {"
# so we print it out 
print(initial_sting)

cnt=len(collaborations_df)
# iterate over the rows of the dataframe:
for i in range(0,cnt):
   # print(collaborations_df.iloc[i,0])
   # print(collaborations_df.iloc[i,1])
   # print(collaborations_df.iloc[i,2])
    print('"' + collaborations_df.iloc[i,0] + '" -> "' + collaborations_df.iloc[i,1] + '"'+' [label="'+str(collaborations_df.iloc[i,2])+'"];')
      

# after we iterate over all rows, we need to "close" the graph
final_string = "}"
# so we print it out 
print(final_string)

