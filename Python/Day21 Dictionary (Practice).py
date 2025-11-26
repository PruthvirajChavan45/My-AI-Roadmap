
"""Dictionary Practice Set - 2"""

#.....1) Leetcode 2418 - sort the people.....
"""
    sort the name of the people based on their 
    heights in decreasing order
"""

names = ["Mary", "Jhon", "Emma"]
heights = [180, 165, 170]

d = {}
for i in range(len(names)): 
    d[heights[i]] = names[i]
d = sorted(d.items(), key=lambda x:x[0], reverse = True)

for i in range(len(d)):
    names[i] = d[i][1]
print(names)
