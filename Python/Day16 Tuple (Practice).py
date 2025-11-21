
"""Tuple Practice Set"""

""".....1) Create a tuple with five numbers and print it."""

# t = (10,20,30,40,50)
# print(t)


""".....2) Access the first and last element of a tuple."""

# t = (10,20,30,40,50)
# first_element = t[0]
# last_element = t[-1]
# print(f"first element : {first_element} and last element : {last_element}")


""".....3) Check whether an element exists in a tuple."""

# t = (10,23,45,3,5,35,34,78)
# a = 34

# for i in range(len(t)): 
#     if t[i] == a: 
#         print("this element exists in the tuple")
#         break
# else: 
#     print("this element does not exist in the tuple")


""".....4) Concatenate two tuples and print the result."""

# t1 = (10,20,30)
# t2 = (40,50,60)

# print(t1 + t2)


""".....5) Repeat a tuple 3 times using the * operator."""

# t = (10,20,30,40,50)
# print(t * 3)


""".....6) Find the maximum and minimum element in a tuple of numbers."""

# t = (10,45,67,34,75,79,30,90,42,53)
# print(f"maximum : {max(t)} and minimum : {min(t)}")


""".....7) Convert a tuple to a list, modify the list, and convert it back to a tuple."""

# t = (10,20,30,40)
# lst = list(t)
# lst.append(50)
# lst.append(60)
# lst.append(70)
# print(tuple(lst))


""".....8) Unpack a tuple of 4 values into 4 variables and print them."""

t = (10,20,30,40)
a,b,c,d = t
print(a,b,c,d)




