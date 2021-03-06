# Basic way to get one or multiple lines of input. Always required to solve questions for coding competitions

# Must include sys module to read inputs automatically
import sys

# 1
# Use this to read one single line from the user
user_input = sys.stdin.readline() 

# 2
# To read multiple lines from the user, need to iterate through while loop
while True:
	line = sys.stdin.readline().rstrip("\n") #rstrip with token "\n" This splits string from user with delimeter, "\n"
	if line == "":
		break
	# do some modification or process in here
	
# Example 1:
# Q. The input is given. The input consists of maximum 100 lines containing only smaller cases, capitals, spaces and numbers
# Each line does not exceed 100 characters and empty line will not be given.
# Also, each line does not start with space nor finish with space.
# Print out the input.

# A.
while True:
	line = sys.stdin.readline().rstrip("\n")
	if line == "":
		break
	print(line)



while True:
	line = sys.stdin.readline.rstrip("\n") #Read the line from the input
	if line == "": #Since empty line will not be given, if it is empty string, this must be end of input (EOF)
		break #So, escape from while loop and done
	print(line) #Otherwise, print the line out
	
	
	
# Example 2:
# Q. The input is given in 2 lines. Find A + B and print it 
# where A is the number given in the first line and B is the number given in the second line
# Input Example:
# 1
# 2
# Expected output:
# 3

# A.
import sys
number_of_lines_processed = 0
result = 0
while number_of_lines_processed < 2:
    line = sys.stdin.readline().rstrip("\n")
    result += int(line)
    number_of_lines_processed += 1
print (result)
