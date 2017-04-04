# Title: Parenthesis
# Retrieved from  ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2012 #G
#

# Q.
# Parenthesis String (PS) consists of two parenthesis symbols ‘(’ and ‘)’ only. 
# In parenthesis strings, some strings are called a valid PS (shortly, VPS). Let us give the formal definition of VPS. 
# A single “( )” is a member of VPS, called the base VPS. Let x and y be a member of VPS. 
# Then “(x)”, a VPS which encloses a VPS x with a single pair of parenthesis, is also a member of VPS. 
# And xy, the concatenation of two VPS x and y, is a member of VPS. For example, “(())()” and ((()))” are all VPS, 
# but “(()(”, “(())()))” and “(()” are not VPS. You are given a set of PS. You should decide if the input string is VPS or not. 
# 
# 
# Input:
# Your program is to read from standard input. The input consists of T test cases. The number of test cases 
# T is given in the first line of the input. Then PS’s are given in the following T lines one by one. 
# The length of each PS is between 2 and 50, inclusively.

# Input Example:
# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

# Output:
# Your program is to write to standard output.
# Print the result in each line. 
# If the input string is a VPS, then print “YES”. Otherwise print “NO”. 

# Expected Output:
# NO
# NO
# YES
# NO
# YES
# NO

import sys

class Stack:
	def __init__(self):
		self.items = []

	def push(self, x):
		self.items.append(x)

	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[-1]
	
	def size(self):
		return len(self.items)
	
	def isEmpty(self):
		return self.items == []

	def __str__(self): #This is not required but for testing purpose
		string = ""
		for i in self.items:
			string += i
		return string

def stackOperation(parenthesis_string):
	stack = Stack()			
	for each_char in parenthesis_string:
		if each_char == "(": # Push all "(" into the stack
			stack.push(each_char)
		elif each_char == ")": # Whenever there is ")" check if the stack is empty 
			if stack.isEmpty(): # If it is empty, there was no opening bracket but having the closing bracket
				return "No" # So, this is not right. Return "No"
			stack.pop() # Otherwise, remove one opening bracket from the stack
	if stack.isEmpty(): #After iterating through the whole string, if it is empty,
		return "Yes" #This is right. Return "Yes"
	return "No" #If there is something left in the slack, there are more opening brackets than closing brackets. This is wrong. Return "No"


number_of_lines = int(sys.stdin.readline().rstrip("\n")) #Read how many lines which are going to be given
for i in range(number_of_lines):
	parenthesis_string = sys.stdin.readline().rstrip("\n") #Read each test case and apply a method
	print(stackOperation(parenthesis_string)) #Print out the result
		
