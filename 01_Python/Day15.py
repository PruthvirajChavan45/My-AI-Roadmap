
"""....2) Tuple in Python...."""
#         - A tuple is a Python data structure used to store multiple items in a single variable.
#         - It is almost like a list, but with one big difference:
#             - Tuple is Immutable (You cannot change, add, remove, or modify items after creation.)

"""....How to Create Tuples...."""

#.....Normal tuple.....
# t = (1, 2, 3)


#.....Single-element tuple — must add comma!.....
# t = (5,)   # correct

# Without comma:
# t = (5)    # this is NOT a tuple, it's an integer


#.....Tuple without parentheses.....
# t = 10, 20, 30      # Tuple packing.




"""....Properties of Tuple...."""

#.....1) Ordered.....
#       - Items have fixed index positions.

# example:
# t = (1, 2, 3)
# index: 0 1 2



#.....2) Immutable (Cannot modify).....
#       - You cannot change any item.

# example:
# t = (10, 20, 30)
# t[1] = 200    # ❌ ERROR



#.....3) Allows duplicates.....

# example:
# t = (1, 1, 2, 2, 3)



#.....4) Can store different data types.....

# example:
# t = (10, "hello", 3.5, True)



#.....5) Supports indexing & slicing.....

# example:
# t = (10, 20, 30, 40)
# print(t[1])      # 20
# print(t[1:3])    # (20, 30)



"""....Unpacking a Tuple...."""

# t = (10, 20, 30)
# a, b, c = t
# print(a, b, c)

#....Output:...
# 10 20 30



"""....Tuple Traversing...."""

#....1) Directly accessing values : 

# a = (10,20,30,40)
# for i in a: 
#     print(a)

#.....output.....
#       10
#       20
#       30
#       40


#....2) On the basis of index (using range function) : 

# a = (10,20,30,40)
# for i in range(len(a)): 
#     print(f"{i} : {a[i]}")

#.....output.....
#      0 : 10
#      1 : 20
#      2 : 30
#      3 : 40



"""....Tuple Methods...."""

#....1) count() — count occurrences :
t = (1, 2, 2, 3)
print(t.count(2))     # 2


#....2) index() — find position of value :
print(t.index(3))     # 3rd index (0-based)
