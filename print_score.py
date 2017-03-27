# Title: Counting Sheep (Small)
# Retrieved from 
# https://www.acmicpc.net/problem/9498

# Q:
# Print Score according to the interger given

# A:


import sys

def scorePrint(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

score = sys.stdin.readline().rstrip("\n")
result = scorePrint(int(score))
print (result)

#
# For better readability, instead of using if~, elif~ , ..., elif~, else~
# I have used if~ return, if~ return ...
# It still produces the same result
