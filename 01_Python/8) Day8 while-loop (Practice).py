"""while-loop Practice Set"""

#.....1) Print Each Digit (Revese Order).....
"""
    Break a number into individual digits and 
    print them starting from the last digit.
"""

# num = int(input("Tell your number : "))

# while num > 0: 
#     digit = num % 10
#     print(digit)
#     num = num // 10


#.....2) Sum of Digits.....
"""
    Add all the digits of a number 
    (e.g., 123 :- 1 + 2 + 3 = 6).
"""

# num = int(input("tell Your Number : "))
# total = 0
# while num > 0: 
#     total = total + num % 10
#     num = num // 10

# print("Your digit Sum is ", total)


#.....3) Reverse a number .....
"""
    input a number and reverses its digit
    (e.g., 123 = 321).
"""

# num = int(input("tell your number : "))
# rev = 0
# while num > 0: 
#     rev = rev * 10 + (num % 10)
#     num = num // 10

# print(f"Your Reversed number is {rev}")


#.....4) Palindrome number check .....
"""
    check if a number reads the same forward and backward
    (e., 121, 1331)
"""

# num = int(input("tell your number : "))
# copy = num
# digit = 0
# while num > 0: 
#     digit = digit * 10 + (num % 10)
#     num = num // 10

# if copy == digit: 
#     print("Your number is palindrome number")

# else: 
#     print("Your number is not palindrome number")


#.....5) Automorphic Number .....
"""
    a number is a automorphic if its square ends with the number
    itself(e.g., 5=25, 76=5776) check and print result.
"""

num = int(input("tell your number : "))
copy = num
square = num ** 2

count = 0
while num > 0: 
    count = count + 1
    num = num // 10

extract = square % (10**count)
if extract == copy: 
    print("Your number is automorphic")
else: 
    print("Your number is not automorphic")







