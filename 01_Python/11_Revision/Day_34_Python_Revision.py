# ---------------- PYTHON MASTER REVISION SHEET ----------------

# 1) BASIC
# --------------------------------------------------------------
# Comments
#   # single
#   """ multi """

# Variables & Datatypes
x = 10
pi = 3.14
name = "John"
flag = True

# Built-in Types: int, float, str, bool, list, tuple, set, dict

# String & Type Conversion
text = "10"
num = int(text)
word = str(50)
flt  = float("2.5")

# String useful
"hello".upper()
"HELLO".lower()
"s".isalpha()



# 2) OPERATORS
# --------------------------------------------------------------
# Arithmetic: +  -  *  /  //  %  **
# Assignment: =  +=  -=  *=  /=
# Comparison: == != > < >= <=
# Logical   : and or not

# Examples
a = 5
b = 2
a+b; a-b; a*b; a/b; a//b; a%b; a**b


# 3) CONDITIONALS
# --------------------------------------------------------------
age = 18
if age > 18:
    print("adult")
elif age == 18:
    print("just 18")
else:
    print("minor")


# 4) LOOPS
# --------------------------------------------------------------
# for loop
for i in range(1,5):
    print(i)

# while loop
n = 1
while n<=5:
    print(n)
    n += 1


# 5) FUNCTIONS
# --------------------------------------------------------------
def add(x,y):
    return x+y

# default argument
def greet(name="Guest"):
    print("Hello",name)

# lambda
square = lambda x: x*x


# 6) DATA STRUCTURE + MAIN METHODS
# --------------------------------------------------------------
# List
l = [1,2,3]
l.append(4)
l.pop()
l.remove(2)

# Tuple (immutable)
t = (10,20,30)

# Set (unique items)
s = {1,2,2,3}
s.add(5)

# Dictionary
d = {"name":"John", "age":25}
d["city"] = "Pune"
d.get("age")
d.keys()
d.values()


# 7) COMPREHENSION / MAP / FILTER
# --------------------------------------------------------------
nums = [1,2,3,4,5]

# list comprehension
sq = [x*x for x in nums]

# map
m = list(map(lambda x: x*2, nums))

# filter
f = list(filter(lambda x: x%2==0, nums))


# 8) EXCEPTION & FILE HANDLING
# --------------------------------------------------------------
try:
    print(10/0)
except ZeroDivisionError:
    print("can't divide")

# finally always runs
finally:
    print("done")

# file
with open("test.txt","r") as f:
    data = f.read()


# 9) OOPS
# --------------------------------------------------------------
# encapsulation (private variable using _ or __)
class A:
    def __init__(self):
        self.__x = 10  

# inheritance
class B(A):
    pass

# polymorphism (same method different class)
class A:
    def show(self): print("A")
class B:
    def show(self): print("B")

# abstraction (hiding detail using method)


# 10) MODULE & PACKAGE
# --------------------------------------------------------------
# Module = single python file
# Package = folder having __init__.py

# import whole
import math
print(math.sqrt(16))

# import specific
from math import sqrt
print(sqrt(16))

# create your own module:
# new file: calc.py
# def add(a,b): return a+b
# in main: from calc import add


# --------------------------------------------------------------
