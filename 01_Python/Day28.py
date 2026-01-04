"""......Encapsulation......"""
#       - Encapsulation means wrapping data (variables)
#         and methods inside a class and restricting direct access from outside.

# In simple words:
#   - Hide the data and protect it.


"""......Access Modifiers......"""
#   1) Public
#   2) Protected
#   3) Private

"""......1) Public......"""
#   - Accessible from anywhere 
#   - Example : self.name

#   public variable : 
#       self.name = "Pruthviraj"


"""......2) Protected......"""
#  - Protected in python : 
#      - Written with one underscore: _variable
#      - Only a naming convention
#      - Not truly protected (can still be accessed)
#      - Tells developer: " internal use only "

#   public variable : 
#       self._salary = 50000


"""......3) Private......"""
#   - Use two underscores __variable
#   - Completely hidden from outside
#   - Cannot be accessed directly.
#   - Example: self.__balance

#   public variable : 
#       self.__balance = 10000


"""......Example......"""

class Demo:
    def __init__(self):
        self.name = "Public Variable"          # Public
        self._salary = 50000                   # Protected
        self.__balance = 100000                # Private


obj = Demo()

# PUBLIC ACCESS
print("\nPublic Access:")
print(obj.name)               # Allowed

# PROTECTED ACCESS (Convention: don't use outside, but allowed)
print("\nProtected Access:")
print(obj._salary)            # Allowed but not recommended

# PRIVATE ACCESS (Not allowed directly)
print("\nPrivate Access:")
print(obj.__balance)        # Error: Attribute not found
