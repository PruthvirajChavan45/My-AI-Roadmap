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
# class Person:
#     def __init__(self, name):
#         self.name = name

# Called automatically when you do:
# p = Person("John")


"""..... 2) String Representation :— __str__ ......"""

# class Student: 
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     # Controls how the object prints.
#     def __str__(self): 
#         return f"Your name is {self.name} and your marks are {self.marks}"
    
# obj = Student("Pruthviraj", 98)
# # When you do:
# print(obj)

# #   - Python calls __str__()


"""..... 3) Operator Overloading :— __add__, __eq__, etc. ......"""

# Example: == operator → __eq__

class Equalto: 
    def __init__(self, number):
        self.number = number

    def __eq__(self, custom):
        return self.number == custom.number

obj1 = Equalto(10)
obj2 = Equalto(10)

print(obj1 == obj2)  # Ture

#.....Python converts:
# obj1 == obj2

#.....into:
# obj1.__eq__(obj2)