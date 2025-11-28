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

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("You must be 18+")
    print("Access granted")
except Exception as e:
    print("Error:", e)

#...Output...
# Enter age: 13
# Error: You must be 18+

