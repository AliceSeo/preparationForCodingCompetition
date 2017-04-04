# This is not done
# Retrieved from 
# https://www.acmicpc.net/problem/2448


import sys
import math


def getString(n):
    '''
    returns a partial string for that nth line
    n starts from 0
    Argument - n: nth row in printed output
    Return - string: partial string needed for nth line
    '''
    additional_space = ""
    if n//3 != 0:
        additional_space = " "
    if n % 3 == 0:   
            return "  *  " + additional_space
    elif n % 3 == 1:
            return " * * " + additional_space
    elif n % 3 == 2:
            return "*****" + additional_space

def getRequiredSpace(n, N):
    '''
    returns string of white spaces needed before and after actual print
    n starts from 0
    Arguments - n: nth row in printed output
    Arguments - N: total number of rows for output
    Return - string: string of white spaces needed before and after actual print
    '''
    WHITE_SPACE = "   "
    return WHITE_SPACE * (N//3 - n//3 - 1)
    
    
		
N = int(sys.stdin.readline().rstrip("\n"))
k = round(math.log(N//3, 2))

for i in range(N):
    space_before = getRequiredSpace(i, N)
    space_after = getRequiredSpace(i, N)
    string = getString(i) * (i//3 + 1)
    print(space_before + string + space_after)

