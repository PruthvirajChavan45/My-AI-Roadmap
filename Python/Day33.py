
"""..... Module ......"""
#   - A module is just a Python file (.py) that contains
#     functions, classes, or variables.

#...Example:
#   - math.py : is a module
#   - random.py : is a module
#   - yourcode.py : is also a module

#....Purpose of a Module
#   - To organize code
#   - To reuse functions
#   - To avoid writing long code in one file.


"""
Example: Creating Our Own Module

File: calculator.py

This file contains calculator functions such as add, subtract, multiply, divide.
This file will behave as a MODULE that can be imported by another Python file.

Path Example: Python/calculator.py
Usage Example:
    import calculator
"""

# import calculator      # importing the calculator module
# print(calculator.add(5, 10))   # calling add() function from the module


"""..... Package ......"""
#      - A package is a folder that contains 
#        multiple Python modules + a special file __init__.py.

# ...Why __init__.py?
#   It tells Python:
#       - "This folder is a package. You can import modules from here."

#.....Package Structure Example :
#    my_package/
#        __init__.py
#        models.py
#        utils.py
#        database.py


# ....Here:
# my_package → Package (folder)
# models.py → Module
# utils.py → Module
# database.py → Module



#....Example:
from mypackage import math_tools, string_tools

print(math_tools.add(3, 7))     # output : 10
print(math_tools.sub(10, 4))    # output : 6

print(string_tools.upper("hello"))  # output : HELLO
print(string_tools.lower("HELLO"))  # output : hello


# ----- Importing Modules From a Package (Example) -----

# Case-1: Import multiple modules from the same package
# from mypackage import math_tools, string_tools

# Now we can use functions of both modules:
# math_tools.add(3, 7)
# math_tools.sub(10, 4)

# string_tools.upper("hello")
# string_tools.lower("HELLO")

