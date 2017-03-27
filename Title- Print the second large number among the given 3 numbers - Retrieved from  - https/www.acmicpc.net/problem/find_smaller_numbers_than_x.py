# Title: Find smaller numbers than X among the given N numbers
# Retrieved from 
# https://www.acmicpc.net/problem/10871

# Q:
# Print the smaller numbers than X among the N numbers given
# 
# Input:
# The first line of the input gives the number of given numbers, N and the number which will be compared to, X. N numbers follow.
# N >= 1
# X <= 10000
# The second line of the input gives all numbers which will be compared to X. 
#
# Input Example:
# 10 5
# 1 10 4 9 2 3 8 5 7 6
#
# Output:
# Find numbers smaller than X and print them in the order as given in the input
# Separate them with a space
#
# Expected output:
# 1 4 2 3

# A:
import sys

def findSmallerThanX(x, numbers):
    string = ""
    for number in numbers:
        if int(number) < x:
            string += number + " "
    return string
first_line = sys.stdin.readline().rstrip("\n")
second_line = sys.stdin.readline().rstrip("\n")
info = first_line.split()
numbers = second_line.split()
x = int(info[1])
result = findSmallerThanX(x, numbers)
print (result)

# Note: before use if ~ > ~, don't forget to change its type from string to int.

