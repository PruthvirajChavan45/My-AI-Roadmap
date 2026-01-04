
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
  
# class Student : 
#     @staticmethod
#     def info():
#         print("This is a student class.")

# Student.info()


""".....Example....."""

# class Animal:
#     gender = "Male" # class attribute

#     def __init__(self,name,age):
#         self.name = name #instance attribute
#         self.age = age  #instance attribute

#     def info(self):  #instance method
#         print("this is a method")
    
#     @classmethod
#     def clmethod(cls): #class method
#         print(f"{cls.gender} is your gender")
    
#     @staticmethod
#     def hello():  #static method
#         print("hello I am a static method")


# obj = Animal("Lion",12)
# obj.info()
# obj.clmethod()
# obj.hello()


""" ....Task....

make a student registration system ask for 
name, age, number, blood group register 3 students 

"""

class Registration: 
    def __init__(self, name, age, number, blood_group):
        self.name = name
        self.age = age
        self.number = number
        self.blood_group = blood_group

    def student_info(self):

        print("\n....Student Information....") 
        print(f"Your name is {self.name}\nYour age is {self.age}\nYour number is {self.number}\nYour Blood group is {self.blood_group}")


s1 = Registration("Pruthviraj", 21, 9021906000, "B+")
s2 = Registration("Raj", 21, 9322831600, "O+")
s3 = Registration("Anil", 41, 8758456345, "AB-")


s1.student_info() 
s2.student_info()
s3.student_info()

