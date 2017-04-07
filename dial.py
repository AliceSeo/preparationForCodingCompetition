# Title: Dial
# Retrieved from Contest > Croatian Open Competition in Informatics > COCI 2012/2013 > Contest #6 #1
# http://hsin.hr/coci/archive/2012_2013/contest6_tasks.pdf

# Q: 
# Mirko's grandma still uses an ancient pulse dial telephone with a rotary dial.
# For each digit that we want to dial, we need to turn the rotary dial clockwise until the chosen digit reaches the finger stop 
# (metal fin). Then we let go of the dial and wait for it to return to its original position before we can dial another digit. 
# In our modern, instant gratification world, the dial return often lasts much longer than our patience. 
# More precisely, dialling the digit 1 takes a total of two seconds, 
# while dialling any larger digit takes an additional second for each additional finger circle counting from 1 to the dialled digit.
# Mirko's grandma remembers phone numbers by memorizing a corresponding word which, when dialled, 
# results in the correct number being dialled. When dialling a word, for each letter, 
# we dial the digit which has that letter written next to it on the dial (for example, the digit 7 for the letter S). 
# For example, the word UNUCIC corresponds to the number 868242. 
#
# Your task is determining, for a given word, the total time required to dial that word.
#
# Input:
# The first and only line of input contains a single word consisting of between 2 and 15 (inclusive) uppercase English letters.
# 
# Input Example:
# UNUCIC
# 
# 
# Output:
# The first and only line of output must contain the required dialling time.
# 
# Expected output:
# 36

# A:
import sys
dictionary = {}
alphabet_list = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

# Making a dictionary
for i in range(len(alphabet_list)):
	word = alphabet_list[i]
	for char in word:
		dictionary[char] = i + 3

# Processing a string from the user

string = sys.stdin.readline().rstrip("\n")
total_time = 0
for char in string:
	total_time += dictionary[char]
print(total_time)	
