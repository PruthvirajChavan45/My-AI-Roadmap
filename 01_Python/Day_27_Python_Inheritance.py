
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
# class A:
#     def showA(self):
#         print("A")

# class B(A):
#     def showB(self):
#         print("B")

# class C(B):
#     def showC(self):
#         print("C")

# c = C()
# c.showA()
# c.showB()
# c.showC()


"""......3) Multiple Inheritance......"""
#   - When one child class inherits from multiple parent classes.

# One child ← Parent1 + Parent2

# Example....

# class Father:
#     def f(self):
#         print("Father")

# class Mother:
#     def m(self):
#         print("Mother")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.f()
# c.m()


"""......4) Hierarchical Inheritance......"""
#   - When one parent class has multiple child classes.

# One parent → Many children

# Example....

# class Vehicle:
#     def start(self):
#         print("Engine started")

# class Car(Vehicle):
#     pass

# class Bike(Vehicle):
#     pass

# c = Car()
# b = Bike()

# c.start()
# b.start()


"""......5) Hybrid Inheritance......"""
#   - A combination of two or more types of inheritance (like hierarchical + multiple).

# Mixed form of inheritance
# (Example: one parent → two children → one child inherits from both children)

# Example....

class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(A):
    def showC(self):
        print("C")

class D(B, C):
    def showD(self):
        print("D")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()

