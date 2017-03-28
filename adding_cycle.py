# Title: Adding cycle
# Retrieved from:
# https://www.acmicpc.net/problem/1110

# There is an integer which is greater than or equal to 0 and smaller than or equal to 99. 
# If this number is smaller than 10, put 0 in front to make it 2 digit number, then add two digits.
# Then concatnate the most right digit from the given number and the most right digit from the result of addition to make a new number.
# Here is an example.
# Let's start from 26.
# 2 + 6 = 8
# The new number will be 68
# 6 + 8 = 14
# Now, the new number will be 84
# 8 + 4 = 12
# Now, the new number will be 42
# 4 + 2 = 6
# Now, the new number will be 26
# This example shows that after 4 cycles, it gives the initial number, 26. Hence the length of the cycle is 4.
# Given N, implement a program which calculates the length of the cycle.

# Input:
# In the first line, an integer, N is given.
# 0 <= N <= 99

# Input Example:
# 26

# Output:
# Print out the length of the cycle

# Expected output:
# 4

# A.


import sys

def add(number_string):
    first_number = int(number_string[0])
    second_number = int(number_string[1])
    total = str(first_number + second_number)
    return number_string[1] + total[-1]

initial_number = sys.stdin.readline().rstrip("\n")
if len(initial_number) < 2:
    initial_number = "0" + initial_number
stop = False
cycle = 0
number = initial_number
while(not stop):
    new_number = add(number)
    if initial_number == new_number:
        stop = True
    cycle += 1
    number = new_number
print(cycle)
