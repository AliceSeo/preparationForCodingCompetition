# Title: Self Numbers
# Retrieved from 
# ACM-ICPC > Regionals > North America > Mid-Central Regional > 1998 Mid-Central Regional Programming Contest #D

# Q:
# In 1949 the Indian mathematician D.R. Kaprekar discovered a class of numbers called self-numbers. 
# For any positive integer n, define d(n) to be n plus the sum of the digits of n. 
# (The d stands for digitadition, a term coined by Kaprekar.) For example, d(75) = 75 + 7 + 5 = 87. 
# Given any positive integer n as a starting point, you can construct the infinite increasing sequence of integers 
# n, d(n), d(d(n)), d(d(d(n))), .... For example, if you start with 33, the next number is 33 + 3 + 3 = 39, 
# the next is 39 + 3 + 9 = 51, the next is 51 + 5 + 1 = 57, and so you generate the sequence
#
# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
#
# The number n is called a generator of d(n). 
# In the sequence above, 33 is a generator of 39, 39 is a generator of 51, 51 is a generator of 57, and so on. 
# Some numbers have more than one generator: for example, 101 has two generators, 91 and 100. 
# A number with no generators is a self-number. 
# There are thirteen self-numbers less than 100: 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, and 97.
#
# Write a program to output all positive self-numbers less than 10000 in increasing order, one per line.
# 
# 
# Input:
# There will be no input
# 
# Output:
# All positive self-numbers less than 10000 in increasing order, one per line
#
#
# Expected output:
# 1
# 3
# 5
# 7
# 9
# 20
# 31
# 42 
# 53
# 64
# |
# |       <-- a lot more numbers
# |
# 9903
# 9914
# 9925
# 9927
# 9938
# 9949
# 9960
# 9971
# 9982
# 9993


# A:

def getGenerated(number):
    number_string = str(number)
    sum_of_each_digit = 0
    for i in range(len(number_string)):
        sum_of_each_digit += int(number_string[i])
    return number + sum_of_each_digit
    
dictionary = {} #use dictionary instead of list because in operation in dictionary is O(1) while in list it is O(n)

for i in range(10000):
    number = getGenerated(i)
    if number < 10000 and number not in dictionary:
        dictionary[number] = 0
        
for i in range(10000):
    if i not in dictionary:
        print(i)
    
