"""......Abstraction......"""
#   - Abstraction = Hiding unnecessary details and showing only what is needed.
#   - It allows the user to focus on what something does, not how it does it.

# Real-life example:
#   - You drive a car → you use steering, brake, accelerator
#   - You don't see engine internals
# This is abstraction.


""".....Abstraction in Python using ABC (Abstract Base Class)......"""
#   - ABC → Abstract Base Class
#   - @abstractmethod → Method that must be implemented in child class

# These are imported from:
# from abc import ABC, abstractmethod


""".....What is an Abstract Class?......"""
# A class that:
#   - Cannot be instantiated (cannot create object directly)
#   - Contains abstract methods
#   - Must be inherited by another class
# Think of it as a template.


""".....What is an Abstract Method?......"""
#   - A method declared in the parent class but does not have implementation.
#   - Child class must override it.

#..Syntax :
#   @abstractmethod
#   def method_name(self):
#       pass


""".....Example of Abstraction......"""

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Child Class (Implementation)
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

obj = Dog()
obj.sound()

