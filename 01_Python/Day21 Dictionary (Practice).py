
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

# s1 = "aabbcc"
# s2 = "baccab"

# if len(s1) == len(s2): 
#     d = {}

#     for i in s1:
#         if i in d.keys(): 
#             d[i] += 1
#         else: 
#             d[i] = 1

#     for i in s2: 
#         if i in d.keys(): 
#             d[i] -= 1
#         else: 
#             print("An extra element was found")

#     for i in d: 
#         if d[i] != 0:
#             print("your elements are not same") 
#             break
#     else: 
#         print("your strings are same")

# else: 
#     print("Strings are not same")



#.....3) Find duplicates in array using hashset.....
"""
    detect and print elements that appear more than once
    in the array.
"""  

# a = [1,1,3,3,3,5,5,6,6,6,3,5,3,2,3,4,6,7,8,8,0]
# d = {}

# for i in a: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1

# for i in d.keys():
#     if d[i] > 1: 
#         print(i) 
    


#.....4) Leetcode 2404 - Most frequenct even element.....
"""
    find the even number with the highest frequency, return 
    the smallest one if ties exist
"""  

# nums = [0,1,6,6,4,4]
# d = {}

# for i in nums: 
#     if i % 2 == 0: 
#         if i in d.keys(): 
#             d[i] += 1
#         else: 
#             d[i] = 1

# if not d: 
#     print(-1)

# max_f = max(d.values())

# cand = [num for num, freq in d.items() if freq == max_f]

# print(min(cand))



#.....5) Leetcode 2283 - check if number has equal digit count and digit value.....
"""
    determine if the count if each digit matches its value in the string.
"""  
# num = "1210"
# d = {}

# for i in num: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1

# for i in range(len(num)): 
#     if d.get(str(i), 0) == int(num[i]): 
#         continue
#     else: 
#         print("False")



#.....6) Intersection of two arrays.....
"""
    return all the unique elements that appear in both arrays.
""" 

a = [1,2,3,4,5]
b = [4,5,6,7,8]

j = []
d = {}
for i in a: 
    if i in d.keys(): 
        d[i] += 1
    else: 
        d[i] = 1

for i in d.keys(): 
    if i in b: 
        j.append(i)
print(j)


