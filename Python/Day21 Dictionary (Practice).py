
"""Dictionary Practice Set - 2"""

#.....1) Leetcode 2418 - sort the people.....
"""
    sort the name of the people based on their 
    heights in decreasing order
"""

# names = ["Mary", "Jhon", "Emma"]
# heights = [180, 165, 170]

# d = {}
# for i in range(len(names)): 
#     d[heights[i]] = names[i]
# d = sorted(d.items(), key=lambda x:x[0], reverse = True)

# for i in range(len(d)):
#     names[i] = d[i][1]
# print(names)


#.....2) Check if two strings have same frequency map.....
"""
    compare character frequencies of two strings and 
    check if they match.
"""

s1 = "aabbcc"
s2 = "baccab"

if len(s1) == len(s2): 
    d = {}

    for i in s1:
        if i in d.keys(): 
            d[i] += 1
        else: 
            d[i] = 1

    for i in s2: 
        if i in d.keys(): 
            d[i] -= 1
        else: 
            print("An extra element was found")

    for i in d: 
        if d[i] != 0:
            print("your elements are not same") 
            break
    else: 
        print("your strings are same")

else: 
    print("Strings are not same")