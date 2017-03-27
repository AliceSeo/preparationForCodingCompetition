# Title: Above Average
# Retrieved from  Waterloo's local Programming Contests > 28 September, 2002 #D
# http://acm.student.cs.uwaterloo.ca/~acm00/

# Q.
# It is said that 90% of frosh expect to be above average in their class. You are to provide a reality check.
# 
# Input:
# The first line of standard input contains an integer C, the number of test cases. 
# C data sets follow. Each data set begins with an integer, N, 
# the number of people in the class (1 <= N <= 1000). N integers follow, 
# separated by spaces or newlines, each giving the final grade (an integer between 0 and 100) of a student in the class. 

# Input Example:
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

# Output:
# For each case you are to output a line giving the percentage of students whose grade is above average, 
# rounded to 3 decimal places.

# Expected Output:
# 40.000%
# 57.143%
# 33.333%
# 66.667%
# 55.556%

# A.
import sys

def findAverage(string_list):
    total = 0
    for i in range(len(string_list) - 1):
        total += int(string_list[i + 1])
        string_list[i+1] = int(string_list[i + 1])
    average = total / int(string_list[0])
    string_list.pop(0)
    return average, string_list

def printFormat(percent):
    numbers = str(percent).split(".")
    if len(numbers[1]) < 3:
        numbers[1] += "0" * (3 - len(numbers[1]))
    return numbers[0] + "." + numbers[1]

number_of_inputs = int(sys.stdin.readline().rstrip("\n"))
for i in range(number_of_inputs):
    number_of_students_above_average = 0
    line = sys.stdin.readline().rstrip("\n")
    scores = line.split()
    t = findAverage(scores)
    average = t[0]
    score_list = t[1]
    for score in score_list:
        if score > average:
            number_of_students_above_average += 1
    percentage = number_of_students_above_average / len(score_list) * 100
    result = printFormat(percentage)
    sys.stdout.write(result)
    sys.stdout.write("%\n")
