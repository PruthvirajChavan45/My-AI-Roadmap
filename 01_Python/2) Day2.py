""".....String...."""

#...1) String Indexing...

# a) Positive Indexing

# a = "NATURE"
# print(a[3])                #output : U

# b) Negative Indexing

# b = "PRUTHVIRAJ CHAVAN"
# print(b[-1])               #output : N



#...2) String Slicing...

# a = "Hello I Am Data Scientist"

# print(a[::])      #output : Hello I Am Data Scientist
# print(a[:5])      #output : Hello
# print(a[11:15])   #output : Data 
# print(a[16:])     ##output : Scientist


#...3) Immutable Nature...

# a = "hzllo"
# a[1] = 'e'    #show error because it is immutable



""".....Print Statement Ways...."""

#....1) Narmal Way....

# name = "Rohit Sharma"
# age = 38

# print("My name is",name,"and my age is",age)

#...output....
# My name is Rohit Sharma and my age is 38



#....2) Formatted String Way....

# name = "Pruthviraj Chavan"
# age = 21

# print(f"My Name is {name} and my age is {age}")   

#...output....
# My Name is Pruthviraj Chavan and my age is 21



""".....Type Conversion...."""

# a = "23"         # string
# a = int(a)       # convert Sring to int

# b = 56           # integer
# b = float(b)     # convert integer to float

# a = 0            # integer
# print(bool(a))   # convert interger to boolean


''' Truthy Values : almost everything 
    Falsy Values : 0, 0.0, False, "", [], {}, () '''



""".....Input Statement...."""

# name = input("Tell Your Name : ")
# age = int(input("Tell Your Age : "))
# print(f"My Name is {name} and My Age is {age}")






