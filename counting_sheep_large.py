# Title: Counting Sheep (Large)
# Retrieved from  Contest > Google Code Jam > Google Code Jam 2016 > Qualification Round #A2
# https://code.google.com/codejam/

# Q.
# Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. 
# First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. 
# Whenever she names a number, she thinks about all of the digits in that number. 
# She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. 
# Once she has seen each of the ten digits at least once, she will fall asleep.

# Bleatrix must start with N and must always name (i + 1) × N directly after i × N. 
# For example, suppose that Bleatrix picks N = 1692. She would count as follows:
# N = 1692. Now she has seen the digits 1, 2, 6, and 9.
# 2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
# 3N = 5076. Now she has seen all ten digits, and falls asleep.
# What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.

# Input:
# The first line of the input gives the number of test cases, T. 
# T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen.
# 1 <= T <= 100
# 0 <= N <= 1000000
#
# Input Example:
# 5
# 0
# 1
# 2
# 11
# 1692
#
# Output:
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and 
# y is the last number that Bleatrix will name before falling asleep, according to the rules described in the statement.
# 
# Expected Output:
# Case #1: INSOMNIA
# Case #2: 10
# Case #3: 90
# Case #4: 110
# Case #5: 5076
#
# A:
import sys

def find_string(n):
	if n == 0:
		return "INSOMNIA"
	current_n = str(n)
	factor = 1
	collection = ""
	while (len(collection) != 10):
		for str_digit in current_n:
			if str_digit not in collection:
				collection += str_digit
		factor += 1
		current_n = str(n * factor)
	return str(n*(factor - 1))
	
	
t = int(sys.stdin.readline().rstrip("\n"))
for row in range(t):
	n = int(sys.stdin.readline().rstrip("\n"))
	result = find_string(n)
	string_to_print = "Case #" + str(row + 1) + ": " + result
	print(string_to_print)
		
		
    
    
# Note: this is exactly the same as 
# https://github.com/AliceSeo/preparationForCodingCompetition/blob/master/counting_sheep_small.py
# This works fine with the larger dataset as well :)
