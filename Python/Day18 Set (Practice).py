"""Set Practice Set"""

""".....1) Create a set with 10 elements."""

# s = {10,20,30,40,50,60,70,80,90,100}
# print(s)


""".....2) Add 2 new elements to an existing set."""

# s = {10,20,30,40,50,60,70,80,90,100}
# s.update([25,35])
# print(s)


""".....3) Remove an element from a set using remove()."""

# s = {10,20,30,40,50,60,70,80,90,100}
# s.remove(40)
# print(s)


""".....4) Remove an element from a set using discard()."""

# s = {10,20,30,40,50,60,70,80,90,100}
# s.discard(50)
# print(s)


""".....5) Check whether a given element exists in a set or not."""

# s = {10,20,30,40,50,60,70,80,90,100}
# search = 30

# if search in s:
#     print("This element exists in the set")
# else:
#     print("This element does not exist in the set")


""".....6) Convert a list with duplicate values into a set."""

# s = [1,1,2,3,4,2,3,2,5]
# s = set(s)
# print(s)


""".....7) Find the length of a set."""

# s = {10,20,30,40}
# print(len(s))


""".....8) Find the union of two sets."""

# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a.union(b))


""".....9) Find the intersection of two sets."""

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a.intersection(b))


""".....10) Find the difference of two sets (A - B)."""

# A = {1,2,3,4}
# B = {3,4,5,6}

# print(A - B)


""".....11) Find the symmetric difference of two sets."""

# A = {1,2,3,4}
# B = {3,4,5,6}

# print(A ^ B)


""".....12) Check if one set is a subset of another."""

# A = {1,2,3,4}
# B = {3,4}

# if A.issubset(B): 
#     print("A is subset of B")

# elif B.issubset(A): 
#     print("B is subset of A")

# else: 
#     print("Both are different")


""".....13) Check if one set is a superset of another."""

# A = {1,2,3,4}
# B = {3,4}

# if A.issuperset(B): 
#     print("A is superset of B")

# elif B.issuperset(A): 
#     print("B is superset of A")

# else: 
#     print("Both are different")



""".....14) Check if two sets are equal."""

# A = {1,2,3,4}
# B = {1,2,3,4}

# if A == B: 
#     print("Both are equal")
# else: 
#     print("Both are not equal")


""".....15) Remove duplicates from a list without using loops (only set)."""

# s = [1,1,2,2,3,4,3,2,5]
# s = set(s)
# print(s)


""".....16) Given two sets, keep only the elements that are unique to both (no common element)."""

a = {10, 20, 30, 40}
b = {40, 50, 60, 70}

result = a ^ b     
print(result)


