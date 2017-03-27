# Title: Find new average
# Retrieved from  https://www.acmicpc.net/problem/1546

import sys

def getIntergerList(scores):
    intList = []
    for score in scores:
        intList += [int(score)]
    return intList

def findNewScores(score_list):
    new_list = []
    maxScore = max(score_list)
    for score in score_list:
        new_score = score / maxScore * 100
        new_list += [new_score]
    return new_list

def findAverage(score_list):
    total = 0
    for score in score_list:
        total += score
    return round(total / len(score_list), 2)

def stringFormat(number): #since the question strictly asked for the string format, without this it will be wrong
    number_string = str(number)
    decimal_point_list = number_string.split(".")
    if len(decimal_point_list[1]) < 2:
        decimal_point_list[1] += '0' * (2 - len(decimal_point_list[1]))
    return decimal_point_list[0] + "." + decimal_point_list[1]

first_line = sys.stdin.readline().rstrip("\n")
second_line = sys.stdin.readline().rstrip("\n")
number_of_subjects = int(first_line)
scores = second_line.split()
score_list = getIntergerList(scores)
new_score_list = findNewScores(score_list)
result = findAverage(new_score_list)
print (stringFormat(result))
