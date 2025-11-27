
"""....Advance Stuff in Python...."""

""".....Lambda Expression......"""
#      - It is known as lambda expression or lambda function.
#      - a small, anonymous (nameless) function.
#      - written in one line.
#      - used when you need a quick function for 
#          for a short time
#      - It is created using (lambda) keyword


#....Syntax :- lambda arguments : expression

#       - you can treat like a mini-function.


#....Examples :- 

# 1) Example: 
# square = lambda x : x ** 2
# print(square(12))       # 144

# # 2) Example: 
# add = lambda a, b : a + b
# print(add(10,10))       # 20



""".....1) Map......"""
#   - Apply function to every item of an iterable
#       and return a new iterable.


#....Syntax :- map(function , iterable)

#....Examples :- 

# 1) Example : 
# a = [1,2,3,4,5]
# l = map(lambda x: x ** 2, a)

# print(list(l))          # [1, 4, 9, 16, 25]


# 2) Example : 
# a = [1,2,3,4,5,6,7,8]

# def square(x): 
#     return x ** 2

# l = map(square, a)
# print(list(l))      # [1, 4, 9, 16, 25, 36, 49, 64]



""".....2) Filter......"""
#   - items from an iterable boased on a condition

#....Syntax :- filter(function , iterable)

#....Examples :- 

# 1) Example: 
# a = [1,2,3,4,5,6]
# l = filter(lambda x: x % 2 == 0,a)
# print(list(l))      # [2, 4, 6]


# 2) Example: 
a = [1,2,3,4,5,6,7,8]

def even(x): 
    return x % 2 == 0

l = filter(even, a)
print(list(l))      # [2, 4, 6, 8]