
"""List Practice Set-2"""

#.....1) Linear Search.....
"""
    search for a given element by checking each 
    element one by one.
"""

# a = [3,4,6,34,59,60,38,96]
# search = int(input("Tell your number: "))

# for i in range(len(a)): 
#     if a[i] == search: 
#         print(f"element found at index {i}")
#         break
# else: 
#     print("Sorry no such element exist")



#.....2) Binary Search.....
"""
    efficiently Search for an element in a sorted list using 
    the divide-and-conquer approach.
"""

# a = [12,14,16,23,25,34,37,45,48,59,68,70]

# search = 13

# start = 0
# last = len(a)-1
# mid = (start + last)//2

# while start <= last:
#     if a[mid] == search:
#         print(f"element found at index {mid}")
#         break
#     elif a[mid] < search:
#         start = mid + 1
#         mid = (start + last)//2
    
#     elif a[mid] > search:
#         last= mid -1
#         mid = (start + last)//2
# else:
#     print("sorry no such element exist")


#.....3) Bubble Sort.....
"""
    sort the list by repeatedly swapping adjacent elements
    if they are in the wrong order.
"""

# a = [56,234,23,24,46,6878,9,674,52,3,12,13,368]

# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]

# print(a)


#.....4) Selection Sort.....
"""
    sort the list by selecting the smallest element in each
    pass and placing it in the correct.
"""

a = [56,234,23,24,46,6878,9,674,52,3,12,13,368]

for i in range(len(a)-1):
    j = i+1
    min = i
    for k in range(j,len(a)):
        if a[k] <a[min]:
            min = k
    
    a[i],a[min] = a[min],a[i]

print(a)
