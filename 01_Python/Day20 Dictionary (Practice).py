"""Dictionary Practice Set"""

#...Hashing....

#.....1) Print Unique elements in list.....
"""
    display all distinct elements present in the given list.
"""

# a = [1,1,1,2,2,2,3,3,3,3,3,4,4,4,5,5,6,6,6,6,7,7]

# d = {}

# for i in a: 
#     if i in d.keys(): 
#         d[i] +=1
#     else: 
#         d[i] = 1

# print(d.keys())


#.....2) Count Frequency of Array elements.....
"""
    count how many times each element appers using
    a dictionary or hash map.
"""

# a = {1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,6,6,6,7}

# d = {}

# for i in a: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1
# print(d)


#.....3) Leetcode 771 - jewels and stones.....
"""
    count how many stones are also jewels
    based on give strings.
"""

# jewels = "aA"
# stones = "aAAbbbb"
# d = {}

# for i in stones: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1

# count = 0

# for i in d.keys(): 
#     if i in jewels: 
#         count += d[i]
# print(count)


#.....4) Leetcode 1832 - pangram check.....
"""
    verify if a sentence contains every letters of the english 
    alphabet at least once.
"""

# sentence = "leetcode"
# d = {}

# for i in sentence: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1

# if len(d.keys()) == 26: 
#     print("True")
# else: 
#     print("False")



#.....5) Leetcode 2351 - first letter to appear twice.....
"""
    find the first character that appears twice in a string.
"""

# s = "abccbaacz"
# d = {}
# for i in s: 
#     if i in d.keys(): 
#         print(i)
#         break
#     else: 
#         d[i] = 1


#.....6) Leetcode 1748 - sum of unique elements.....
"""
    return the sum of elements that appear exactly
    once in the array.
"""

a = [1,2,3,2,4,5]
d = {}

for i in a: 
    if i in d.keys(): 
        d[i] += 1
    else: 
        d[i] = 1
sum = 0
for i in d: 
    if d[i] == 1: 
        sum += i
print(sum)


