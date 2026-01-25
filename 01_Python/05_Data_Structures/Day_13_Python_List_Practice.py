
"""List Practice Set"""

#.....1) Sum and average of list.....
"""
    create a list of numbers, then calculate and print 
    the total sum and average.
"""

# a = [10,20,30,40]
# total_sum = 0
# for i in a: 
#     total_sum = total_sum + i

# print(f"Total sum is {total_sum} and their average is {total_sum/len(a)}")



#.....2) Maximum element with index.....
"""
    find the largest element in the list along with 
    it's position (index).
"""

# a = [1,4,2,4,56,7,46,9,90]
# largest = a[0]
# index = 0

# for i in range(len(a)): 
#     if a[i] > largest: 
#         largest = a[i]
#         index = i
# print(f"Your Maximum element is {largest} at index {index}")



#.....3) Second Greatest element.....
"""
    identify the second-largest element in the list 
    without sorting directly.
"""

# a = [3,2,43,56,75,46,90,89]

# max = a[0]
# max2 = a[0]
# index = 0
# index2 = 0

# for i in range(len(a)): 
#     if a[i] > max: 
#         max2 = max
#         index2 = index
#         max = a[i]
#         index = i

#     elif a[i] > max2: 
#         max2 = a[i]
#         index2 = i

# print(f"Your maximum number is {max} at {index}")
# print(f"Your Second maximum number is {max2} at {index2}")



#.....4) Check if list is sorted (increasing).....
"""
    verify whether the list elements are in ascending order.
"""

# a = [1,2,3,4,5,6]

# for i in range(len(a)-1): 
#     if a[i] < a[i+1]: 
#         continue
#     else: 
#         print("This number is not sorted")
#         break
# else: 
#     print("Your list is sorted")



#.....5) Left Rotation By 1 .....
"""
    shift all elements one position to the left, with the first element 
    moving to the end.
"""

# a = [10,20,30,40,50]

# for i in range(len(a)-1): 
#     a[i],a[i+1] = a[i+1],a[i]
# print(a)



#.....6) Right Rotation By 1 .....
"""
    shift all elements one position to the right, with the last element 
    moving to the first.
"""

# a = [10,20,30,40,50]

# for i in range(len(a)-1,0,-1): 
#     a[i],a[i-1] = a[i-1],a[i]
# print(a)



#.....7) Left Rotation By k .....
"""
    generalize the previous problem: 
    rotate the list by k time to the left.
"""

# k = int(input("How many times you want to rotate : "))
# a = [10,20,30,40,50]

# for i in range(k): 
#     for i in range(len(a)-1): 
#         a[i], a[i+1] = a[i+1], a[i]

# print(a)



#.....8) Reverse List (In-Place ).....
"""
    reverse the entire list without using extra space
    [i.e., swap elements.]
"""

a = [10,20,30,40,50]
b = len(a) - 1

for i in range(len(a)//2): 
    a[i],a[b] = a[b],a[i]
    b = b - 1
print(a)
