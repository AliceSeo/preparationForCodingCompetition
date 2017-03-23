# Title: ŠEĆER
# Retrieved from Croatian Open Competition in Informatics > COCI 2010/2011 > Contest #7
# Q.
# Mirko works in a sugar factory as a delivery boy. He has just received an order: he has to deliver exactly N kilograms
# of sugar to a candy store on the Adriatic coast. Mirko can use two types of packages, the ones that contain 3 kilograms,
# and the ones with 5 kilograms of sugar.
# Mirko would like to take as few packages as possible. For example, if he has to deliver 18 kilograms of sugar, 
# he could use six 3-kilogram packages. But, it would be better to use three 5-kilogram packages, and one 3-kilogram
# package, resulting in the total of four packages.
# Help Mirko by finding the minimum number of packages required to transport exactly N kilograms of sugar.

# Input:
# The first and only line of input contains one integer N (3 ≤ N ≤ 5000).
#
# Input Example:
# 18
#
#
# Output:
# The first and only line of output should contain the minimum number of packages Mirko has to use. 
# If it is impossible to deliver exactly N kilograms, output -1.
#
# Expected Output:
# 4
#
# A:

import sys

def getAllCombination(n):
    combination_list = []
    a = 0
    while (n - 5 * a) >= 0:
        if (n - 5 * a) % 3 == 0:
            combination_list += [a + ((n - 5 * a) // 3)]
        a += 1
    return combination_list
    
n = int(sys.stdin.readline().rstrip("\n"))
combination_list = getAllCombination(n)
if len(combination_list) == 0:
    print (-1)
else:
    print(min(combination_list))



# A. (with explanation)
# N = 5a + 3b where a is the number of 5kg bags and b is the number of 3kg bags 
# Make b as subject of the equation :  
# (N - 5a) / 3 = b
# It is certain that a and b must be whole numbers.
# so, it must be (N - 5a) % 3 == 0 to get b.
# if not, we don't need to try all other values since b will be not calculated with the given a
# use this feature to reduce the calculation time


import sys #for getting inputs

def getAllCombination(n): #defining a separate function for later usability (maybe don't need it tho)
    combination_list = [] #this will contain all possible values of a+b
    a = 0 #start from a = 0, substitude all a until 5a reaches N
    while (n - 5 * a) >= 0: #if 5a is larger than n, we don't need to look at it anymore. range out of bound
        if (n - 5 * a) % 3 == 0:
            combination_list += [a + ((n - 5 * a) // 3)] #do integer divison to avoid making it float
        a += 1
    return combination_list
    
n = int(sys.stdin.readline().rstrip("\n")) #get an input, make sure convert it into int
combination_list = getAllCombination(n) 
if len(combination_list) == 0: #if the list is empty, then no combination is availble
    print (-1)
else: #if there it at least one, print out the minimum
    print(min(combination_list))
