
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

# d1 = {}                                      # empty
# d2 = {"a": 1, "b": 2, "c": 3}                 # with values
# d3 = dict(name="Alex", age=30)               # using dict()
# d4 = dict([("x", 10), ("y", 20)])            # from list of tuples


"""....Adding / Updating Elements...."""

# student = {
#     "name": "Pruthviraj",
#     "age": 22,
#     "course": "Python"
# }

# student["age"] = 23       # update
# student["city"] = "Pune"  # add

# print(student)
# {'name': 'Pruthviraj', 'age': 23, 'course': 'Python', 'city': 'Pune'}


"""....Removing Elements (Function and Their Usage)...."""

# pop(key)      - Removes & returns value
# popitem()     - Removes last inserted key–value pair
# del dict[key] - Deletes key
# clear()       - Removes all items


#.....Example :

# student = {
#     "name": "Pruthviraj",
#     "age": 22,
#     "course": "Python"
# }

# student.pop("age") 
# student.popitem()            
# del student["name"]
# student.clear()


"""....Looping in Dictionary...."""

#.....Example :

# student = {
#     "name": "Pruthviraj",
#     "age": 22,
#     "course": "Python"
# }

# for key in student:
#     print(key) # print keys only.

# for value in student.values():
#     print(value) # print values only.

# for k, v in student.items():
#     print(k, v) # print keys and values.


"""....Dictionary Useful Methods...."""

# keys()    - returns all keys
# values()  - returns all values
# items()   - returns key–value pairs
# update()  - merges 2 dictionaries
# copy()    - creates shallow copy
# setdefault() - returns value of key, if not present inserts it


"""....Nested Dictionary...."""

# students = {
#     1: {"name": "Pruthviraj", "age": 21},
#     2: {"name": "Rohan", "age": 22}
# }
# print(students[1]["name"])  # Pruthviraj


"""....Convert Between Dictionary & Other Data Types...."""

# Tuple of tuples → dict
dict(((1, "A"), (2, "B")))

# List of tuples → dict
dict([(1, "A"), (2, "B")])



