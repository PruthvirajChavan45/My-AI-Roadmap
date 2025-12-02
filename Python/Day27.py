
"""......Inheritance......"""
#   - Inheritance is the mechanism by which a class (child) can
#     use the properties and methods of another class (parent).

"""......Types of Inheritance ......"""

"""......1) Single-Level Inheritance......"""
#   - When one child class inherits from one parent class.

# One parent → One child

# Example....
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):   # child inherits Animal
    pass

d = Dog()
d.sound()

