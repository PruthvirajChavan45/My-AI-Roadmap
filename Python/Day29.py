"""......Polymorphism......"""
#   - Polymorphism means one thing having many forms.
#   - Polymorphism allows different classes to define methods with the 
#     same name but different behaviors.
#   - In Python, it is typically achieved through method overriding.

"""......Types of Polymorphism......"""
#   1) Method Overloading
#   2) Method Overriding 

"""......1) Method Overloading......"""
#   - Python simulates method overloading using default or variable - length 
#     arguments, as it doesn't support traditional overloading.
#   - same method name, different number of parameters with same class. 
#   - this happens in languages like java / c++ 
#   - Python does ot support this style


#....Example (This does NOT work in Python):.

class Demo:
    def show(self, a):
        print(a)

    def show(self, a, b):  # This replaces the first one
        print(a + b)

#   - Python will keep only the last show() method.
#   - So this is NOT real overloading.