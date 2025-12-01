
"""......Constructor......"""

#   - A constructor is a special method in a class that runs
#     automatically when an object is created.
#   - Constructor is a special method named __init__.
#   - Used to initialize object data.
#   - self refers to the current object.
#   - self.var creates instance variables.


#.......Constructor Example (Simple) :

# class Student:
#     def __init__(self, name, age):
#         self.name = name      # instance variable
#         self.age = age        # instance variable

# s1 = Student("Raj", 20)

#....What happens:

# Object s1 is created
# Constructor runs
# self becomes s1
# s1.name = "Raj"
# s1.age = 20


"""......Attributes and Methods......"""

"""......1) Instance attribute......"""
#   - A attribute created using the self keyword. 
#     (like - self.name, self.age etc)


"""......2) Class attribute......"""
#   - Attribute created inside a class without using the self keyword.

#....example : 
# class Student: 
#     school = "DPS"   # class Attribute


"""......Difference Between instance attribute and class attribute......"""

# class Student:
#     school = "DPS"                # class attribute

#     def __init__(self, name):
#         self.name = name          # instance attribute


"""......Methods......"""

"""......1) Instance Method......"""
#   - A Method created using the self key word as a first parameter.

#....example :                                                     
# class Student:
#     def show(self):
#         print(self.name)

# s1 = Student()
# s1.show()


"""......2) Class Method......"""
#   - A method that works on class attributes.

#...must have - 
#    @classmethod :- decorator
#   cls :- as first argument

#....example :                                                     

# class Student : 
#     @classmethod
#     def change_school(cls, new): 
#         cls.school = new

# Student.change_school("ABC")    # ABC


"""......3) Static Method......"""
#   - A method that does not use object data and does not use class data.

#   Used for utility/helper functions.

#...must have - 
#    @staticmethod :- decorator
#    (no self, no cls)

#....example :
  
class Student : 
    @staticmethod
    def info():
        print("This is a student class.")

Student.info()

