# Title: Print the second large number among the given 3 numbers
# Retrieved from 
# https://www.acmicpc.net/problem/10817

# Q:
# Print the second large number among the 3 numbers given

# A:

import sys

def findSecondLarge(numbers):
    return sorted(numbers)[1]

line = sys.stdin.readline().rstrip("\n")
numbers = line.split()
result = findSecondLarge(numbers)
print (result)

#
# This can be done without using if-elif-else statements
# But this question is supposed to be solved by using if-else statements, I uploaded another possible solution
#


# A:

import sys

def findSecondLarge(numbers):
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    if a >= b and a >= c:
        if b > c:
            return b
        return c
    if b >= a and b >= c:
        if a > c:
            return a
        return c
    if c >= a and c >= b:
        if a > b:
            return a
        return b

line = sys.stdin.readline().rstrip("\n")
numbers = line.split()
result = findSecondLarge(numbers)
print (result)

# Note that when you try to implement this with if-else, it is important to think of the case when all 3 numbers are equal
#

