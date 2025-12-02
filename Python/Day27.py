
"""......Inheritance......"""
#   - Inheritance is the mechanism by which a class (child) can
#     use the properties and methods of another class (parent).

"""......Types of Inheritance ......"""

"""......1) Single-Level Inheritance......"""
#   - When one child class inherits from one parent class.

# One parent → One child

# Example....
# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):   # child inherits Animal
#     pass

# d = Dog()
# d.sound()


"""......2) Multilevel Inheritance......"""
#   - When a class inherits from a child class, forming a chain.

# Parent → Child → Grandchild

# Example....
class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(B):
    def showC(self):
        print("C")

c = C()
c.showA()
c.showB()
c.showC()

