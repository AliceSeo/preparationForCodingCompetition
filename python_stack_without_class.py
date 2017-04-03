# Title: Stack without a class
# 
# Q:
# Implement a stack which takes only integers with 5 basic commands.
# Below is the list of commands
# 
# push x : push the item x into the stack.
# pop : pop the item located on the top of the stack and print it out. If the stack was initially empty, print -1.
# size : print the size of stack.
# empty : print 1 if the stack is empty, otherwise print 0.
# top: print the top element from the stack. If the stack was initally empty, print -1.
#
#
#
#
# Input:
# The first line will contain the number of commands. Then from the second line, commands will be listed.
#
# Input Example:
# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top
#
#
#
# Output:
# Print out the result of commands by line if there needs some print out
#
# Expected Output:
# 2
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3
#
# A:

import sys

def push(x, stack):
	stack.append(x)
	
def pop(stack):
	if len(stack) == 0:
		return -1
	else:
		element = stack[-1]
		stack.pop()
		return element
		
def size(stack):
	return len(stack)
	
def empty(stack):
	if len(stack) == 0:
		return 1
	else:
		return 0
	
def top(stack):
	if len(stack) == 0:
		return -1
	else:
		return stack[-1]
	
stack = []	
number_of_orders = int(sys.stdin.readline().rstrip("\n"))
for i in range(number_of_orders):
	order = sys.stdin.readline().rstrip("\n")
	order_buffer = order.split()
	if order_buffer[0] == "push":
		push(int(order_buffer[1]), stack)
	elif order_buffer[0] == "pop":
		print(pop(stack))
	elif order_buffer[0] == "size":
		print(size(stack))
	elif order_buffer[0] == "empty":
		print(empty(stack))
	elif order_buffer[0] == "top":
		print(top(stack))
