""".....Exception Handling......"""

#   - Exceptions are raised when the program is syntactically
#       correct, but the code results in an error. this error does not 
#       stop the execution of the program, however, it changes the 
#       normal flow of the program.

#   - So you cannot handle the syntax error. but if there is no syntax error 
#      you can handle them.


""".....Exception Handling Functionalities......"""

# Try    : this will catch the exception if any and pass to 
# Except : Except will deal with exception you can have custom 
#          exceptions or universal catcher.
# Else   : Else will be executed if no exception occurs or it 
#           want be executed.
# Finally : This will definitely run no matter what happens.  
# Raise   : Raise a custom error as you need.



#.....Example (try - except - else - finally) :

# a = int(input("provide your numbers : -"))
# b = int(input("provide your numbers : -"))

# try:
#     print(a/b)

# except Exception as err:
#     print(f"sorry an error occured as {err}")

# else:
#     print("there was no erros ")


# finally:
#     print("I will execute no matter what !!")

# print(a+b)



#.....Example of raise :

# try:
#     age = int(input("Enter age: "))
#     if age < 18:
#         raise Exception("You must be 18+")
#     print("Access granted")
# except Exception as e:
#     print("Error:", e)

#...Output...
# Enter age: 13
# Error: You must be 18+



""".....File Handling......"""

#   - File handling in python, as the name suggests  
#     it deals with files with python.
#   - that means creating, reading, updating, and deleting (CRUD)
#     operations in different files.


""".....File Handling Functionalities......"""

#  open() -  to open a file we need to write open() it accepts two 
#            parameters, 1st location of the file , 2nd mode of the
#            file("r", "a", "w", "x")

#....Modes :

# "r" - for reading the file . error if file does not exist.
# "a" - for appending in file. creates a file as well. 
# "w" - overwriting the file. Creates if it does not exist. 
# "x" - creates a file . error if file already exist. 


#......Example.....

# open("pull.txt",'x')  # creating a file

# file = open("push.txt",'w')  # creating a file and writing the content
# file.write("hello this is a sample file that I have created") # content

# file = open("push.txt",'a')  # appeding the content
# file.write("Appended Content")

# file.close() #close the file


"""..... with open() Functionalitie ......"""
#   - This With functionality will open the file and 
#        automatically closes the file once you are done. 

with open("Python/Day19.py",'r') as fs:
     print(fs.read())

