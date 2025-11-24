
"""....4) Dictionary in Python...."""
#   A dictionary is a collection of key–value pairs.

#   Syntax :
#       dict_name = {key: value, key: value, ...}

#.....Example : 

# student = {
#     "name": "Pruthviraj",
#     "age": 22,
#     "course": "Python"
# }


"""....Properties of a Dictionary...."""

# 1) Ordered  -  Yes (Python 3.7+)
# 2) Mutable	- Yes
# 3) Duplicate keys allowed - No
# 4) Indexing - Based on keys
# 5) Heterogeneous values	- Allowed


"""....Creating a Dictionary...."""

d1 = {}                                      # empty
d2 = {"a": 1, "b": 2, "c": 3}                 # with values
d3 = dict(name="Alex", age=30)               # using dict()
d4 = dict([("x", 10), ("y", 20)])            # from list of tuples

