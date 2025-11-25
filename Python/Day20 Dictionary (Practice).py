"""Dictionary Practice Set"""

#...Hashing....

#.....1) Print Unique elements in list.....
"""
    display all distinct elements present in the given list.
"""

a = [1,1,1,2,2,2,3,3,3,3,3,4,4,4,5,5,6,6,6,6,7,7]

d = {}

for i in a: 
    if i in d.keys(): 
        d[i] +=1
    else: 
        d[i] = 1

print(d.keys())




