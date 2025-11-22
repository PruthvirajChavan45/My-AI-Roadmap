
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

