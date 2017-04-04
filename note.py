# Title: Note
# Retrieved from Contest > Croatian Open Competition in Informatics > COCI 2009/2010 > Contest #1 #1
# https://www.acmicpc.net/problem/2920

# Q: 
# C major scale consists of 8 tones: c d e f g a h C. 
# For this task we number the notes using numbers 1 through 8. 
# The scale can be played ascending, from 1 to 8, descending, from 8 to 1, or mixed. Write a program that, 
# given the sequence of notes, determines whether the scale was played ascending, descending or mixed.
#

# Input:
# First and only line of input will contain 8 integers, from 1 to 8 inclusive. Each integer will appear exactley once in the input.
# 
# Input Example:
# 1 2 3 4 5 6 7 8
# 
# 
# Output:
# In the first and only line of input print "descending" if the scale was played descending, "ascending" 
# if the scale was played ascending and "mixed" if the scale was played mixed.
# 
# Expected output:
# ascending

# A:
import sys

def is_ascending(number_list):
	for i in range(len(number_list)):
		if number_list[i] != (i + 1):
			return False
	return True

def is_descending(number_list):
	for i in range(len(number_list)):
		if number_list[i] != 8 - i:
			return False
	return True
		
def make_number_list(string):
	string_list = string.split()
	number_list = []
	for i in range(len(string_list)):
		number_list += [int(string_list[i])]
	return number_list

def main():	
	string = sys.stdin.readline().rstrip("\n")
	number_list = make_number_list(string)
	if is_ascending(number_list):
		print("ascending")
		return
	if is_descending(number_list):
		print("descending")
		return
	print("mixed")
	return

main()
	
