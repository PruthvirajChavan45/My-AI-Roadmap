""".....Dunder/Magic Methods......"""
#   - Dunder = Double UNDERSCORE
#   - These are special methods whose names 
#     start and end with __ (double underscore).

# Example:
# __init__, __str__, __len__, __add__, __eq__

# Why “magic”?
#   - Because Python automatically calls them behind the scenes.


""".....Types of Dunder Methods......"""

"""..... 1) Object Creation :— __init__ ......"""

# Used when object is created.
class Person:
    def __init__(self, name):
        self.name = name

# Called automatically when you do:
p = Person("John")