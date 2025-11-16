

"""............. Arithmetic Operator ............"""

# num1 = 6
# num2 = 3

# print(f"Addition of {num1} + {num2} = {num1 + num2}")
# print(f"Substraction of {num1} - {num2} = {num1 - num2}")
# print(f"Multiplication of {num1} * {num2} = {num1 * num2}")
# print(f"Division of {num1} / {num2} = {num1 / num2}")
# print(f"Floor Divison of {num1} // {num2} = {num1 // num2}")
# print(f"Modulo Division of {num1} % {num2} = {num1 % num2}")
# print(f"exponential of {num1} ** {num2} = {num1 ** num2}")


#.....Output......

# Addition of 6 + 3 = 9
# Substraction of 6 - 3 = 3
# Multiplication of 6 * 3 = 18
# Division of 6 / 3 = 2.0
# Floor Divison of 6 // 3 = 2
# Modulo Division of 6 % 3 = 0
# exponential of 6 ** 3 = 216


"""............. Assignment Operator / Shorthand Operators ............"""

#...Assignment Operator : =
# The assignment operator is used to store a value in a variable.

# x = 10
# y = 5
# name = "Pruthviraj"

#...Shorthand Operators : (+=, -=, *=, /=, //=, %=, **=) 

# x = 10

# x += 5   # x = x + 5 → x becomes 15
# x -= 3   # x = x - 3 → x becomes 12
# x *= 2   # x = x * 2 → x becomes 24
# x /= 4   # x = x / 4 → x becomes 6.0
# x %= 5   # x = x % 5 → x becomes 1.0



"""............. Comparison Operators ............"""

# Comparison Operators : ( ==, !=, >, <, >=, <= )

# a = 10
# b = 12

# print(a == b)       # False
# print(a != b)       # True
# print(a > b)        # False
# print(a < b)        # True
# print(a >= b)       # False
# print(a <= b)       # True


"""............. Logical Operators ............"""

# Logical Operators : ( and, or, not )

#.... 1) and....
# The and operator gives True only when all conditions are True.
# If any one condition is False, result will be False.

print((12 == 12) and (56 != 77))     # output : True
print((43 < 45) and False)           # output : False

#.... 2) or....
# The or operator gives True if at least one condition is True.
# It only gives False when both conditions are False.

print((22 >= 25) or (34 != 55))      # output : True
print((10 != 10) or False)           # output : False


#.... 3) not....
# If something is True, not will make it False
# If something is False, not will make it True

x = True
print(x)     # Output: True

x = True
print(not x)   # Output: False

y = False
print(not y)   # Output: True

