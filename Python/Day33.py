
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

import calculator      # importing the calculator module
print(calculator.add(5, 10))   # calling add() function from the module

