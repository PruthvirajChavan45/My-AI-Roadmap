
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


# # 2) Example: 
# a = [1,2,3,4,5,6,7,8]

# def even(x): 
#     return x % 2 == 0

# l = filter(even, a)
# print(list(l))      # [2, 4, 6, 8]



""".....3) zip......"""
#   - Combine multiple iterables into pairs of elements.

#....Syntax :- zip(iterable 1,iterable2, ....)

#....Examples :- 

# names = ["Pruthviraj", "Ganesh", "Raj"]
# ages = [21, 22, 14]

# comb = zip(names, ages)
# print(list(comb))       # [('Pruthviraj', 21), ('Ganesh', 22), ('Raj', 14)]



""".....Comprehensions......"""

""".....1) List Comprehension......"""

# a = [1,2,3,4,5,6,7,8]
# l = [i for i in a if i % 2 == 0]
# print(l)    # [2, 4, 6, 8]


""".....2) set Comprehension......"""

# a = [1,2,3,4,5,6,7,8]
# l = {i for i in a if i % 2 == 0}
# print(l)    # {8, 2, 4, 6} unordered nature 


""".....3) Dictionary Comprehension......"""

# a = [1,2,3,4,5,6]
# l = {i:i**2 for i in a if i % 2 == 0}
# print(l)    # {2: 4, 4: 16, 6: 36}




""".....Generator......"""
#   - Generators are a special type of iterator that 
#      generate items one by one instead of storing the entire sequence in memory.

#   - Why use them:
#       - Saves memory for large datasets
#       - Efficient for lazy evaluation (compute values only when needed)

#....Examples :- 
# def my_generator():
#     for i in range(5):
#         yield i

# gen = my_generator()
# print(next(gen))    # 0
# print(next(gen))    # 1
# print(list(gen))    # [2,3,4]


""".....Generator Expression......"""

sequence = (x**2 for x in range(5))

print(next(sequence))   # 0
print(next(sequence))   # 1
print(next(sequence))   # 4
