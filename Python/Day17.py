
"""....3) Set in Python...."""

#  - A set is a built-in data structure in Python used to store 
#    multiple items in a single variable, but:

#       - Order is NOT guaranteed.
#       - Duplicate values are NOT allowed.


"""....Properties of a Set...."""

# 1) Unordered  -  No fixed index / arrangement
# 2) Unindexed	- Cannot access values by index
# 3) No duplicates - Automatically removes repeated values
# 4) Mutable - You can add or remove elements
# 5) Mixed data allowed	- Integers, strings, floats, etc.


"""....Example...."""

# s = {10, 20, 30, 20, 30}
# print(s)

#....output.....
# {10, 20, 30}

#   - Duplicates are automatically removed.


"""....Creating a Set...."""

# s = {1, 2, 3}

# #.....Empty set : 

# s = set()      # correct
# s = {}         # ❌ creates dictionary, not set


"""....Set Traversing...."""

#   - Traverse on the basis of values - it will run on the basis 
#       of hash values.
#   - unordered traversing always. 
#   - No index values so no traversing on the basis of index.


"""....Set Methods...."""

""".....Adding and Removing Elements....."""

# s = {10,20,30,40}

# s.add(50)  # Add an element
# s.update([60, 70, 80])   # Add multiple elements
# s.remove(20)   # Remove an element (error if element doesn't exist)
# s.discard(20)  # Remove safely (no error if element not present)
# s.pop()        # Remove random element
# s.clear()      # Clear entire set 


""".....Set Operations....."""

# 1) Union        -  A | B    or     A.intersection(B)
# 2) Intersection -  A & B    or     A.intersection(B)
# 3) Difference   -  A - B    or     A.difference(B)
# 4) Symmetric    -  A ^ B    or     A.symmetric_difference(B)
#    Difference


#....Example....

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union
print(A & B)   # Intersection
print(A - B)   # Difference
print(A ^ B)   # Symmetric Difference

#....Output....

{1, 2, 3, 4, 5, 6}
{3, 4}
{1, 2}
{1, 2, 5, 6}





