"""......Loops......"""
# when we want to perform repetitive task we use loops.
# ...types of loops: 
# 1) for loop 
# 2) while loop


"""....1) for loop...."""
#      - used when we know the number of repetitions in advance. 
#      - controlled by sequence / range.
#      - range function (start, stop, steps)

#....example :-
# for i in range(1,6,1): 
#     print(i)

#....output....
# 1
# 2
# 3
# 4
# 5

""".... for loop on string ...."""
# string is a sequence of characteers.

#....example :-
# word = "PYTHON"
# for i in word: 
#     print(i)

#....output....
# P
# Y
# T
# H
# O
# N


""".... for loop with index (using len() and range() )...."""

#....example :-

name = "PRUTHVI"
for i in range(len(name)): 
    print(i, name[i])

#....output....
#   0 P
#   1 R
#   2 U
#   3 T
#   4 H
#   5 V
#   6 I
