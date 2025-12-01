
"""......Constructor......"""

#   - A constructor is a special method in a class that runs
#     automatically when an object is created.
#   - Constructor is a special method named __init__.
#   - Used to initialize object data.
#   - self refers to the current object.
#   - self.var creates instance variables.


#.......Constructor Example (Simple) :

class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable

s1 = Student("Raj", 20)

#....What happens:

# Object s1 is created
# Constructor runs
# self becomes s1
# s1.name = "Raj"
# s1.age = 20

