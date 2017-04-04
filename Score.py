# Title: Score
# Retrieved from ACM-ICPC > Regionals > Asia > Korea > Asia Regional - Seoul 2005 #A
# https://www.acmicpc.net/problem/8958

# Q: 
# There is an objective test result such as “OOXXOXXOOO”. An ‘O’ means a correct answer of a problem and an ‘X’ means a wrong answer. 
# The score of each problem of this test is calculated by itself and its just previous consecutive ‘O’s only when the answer is correct. 
# For example, the score of the 10th problem is 3 that is obtained by itself and its two previous consecutive ‘O’s. 
#
# Therefore, the score of “OOXXOXXOOO” is 10 which is calculated by “1+2+0+0+1+0+0+1+2+3”. 
#
# You are to write a program calculating the scores of test results. 

# Input:
# Your program is to read from standard input. 
# The input consists of T test cases. The number of test cases T is given in the first line of the input. 
# Each test case starts with a line containing a string composed by ‘O’ and ‘X’ and the length of the string is more than 0 
# and less than 80. There is no spaces between ‘O’ and ‘X’. 
# 
# Input Example:
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
# 
# 
# Output:
# Your program is to write to standard output. Print exactly one line for each test case. 
# The line is to contain the score of the test case. 
# 
# Expected output:
# 10
# 9
# 7
# 55
# 30
# 

# A:
import sys

def get_score(string):
	score_total = 0
	previous_score = 0
	for char in string:
		if char == "O":
			previous_score += 1
			score_total += previous_score
		else:
			previous_score = 0
	return score_total
		
number_of_lines = int(sys.stdin.readline().rstrip("\n"))

for i in range(number_of_lines):
	string = sys.stdin.readline().rstrip("\n")
	print(get_score(string))
