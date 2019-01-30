data=[6,9,10,7,4]

for item in data:
    print(item)

labels=['none','minimal','supervised','independent','professional']
index=labels.index('professional')
answer0=data[index]
print(answer0)

data_dict={'none':6, 'minimal':9,'supervised':10,'independent':7,'professional':4}
answer1=data_dict['professional']
print(answer1)

#Data can be converted from lists to dictionaries 
#taking advantage of the zip function, which combines
#multiple lists of the same length into a single list of tuples 
#(in Python tuples are like lists, but they are constant, 
# i.e. 'immutable')
list(zip(labels,data))#tuples
data_dict_new=dict(zip(labels,data))
#Functions to convert keys and values to lists: data_dict_new.keys(), data_dict_new.values()

#two lists. familiarity with Python and Jave
data_table=[[6,9,10,7,4],[4,10,13,5,4]]
print(data_table[1][2])#familiarity with Jave: supervised

#alternative: use a dictionary with lists as values
data_dict_list={'python':[6,9,10,7,4],'java':[4,10,13,5,4]}
#alternative 2: a dictionary containing dictionaries as values
data_dict_double = {'python': {'none': 6, 'minimal': 9, 'supervised': 10, 'independent': 7, 'professional': 4}, 'java': {'none': 4, 'minimal': 10, 'supervised': 13, 'independent': 5, 'professional': 4} }

data_dict_double['java']['supervised']