# Title: Stack with a class
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

# Class definition: Below is just basic stack class.

class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		if len(self.items) == 0:
			return True
		else:
			return False
			
	# Better way to do this
	#def isEmpty(self):
	#	return self.items == []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()
		
	def peek(self):
		return self.items[-1]
	
	def size(self):
		return len(self.items)
		
# But because this question requires some special conditions (i.e. print out -1 if pop command is used when stack is empty), this class should be modified
# Or, maybe use if-else statements outside of the class. But this time, I will implement these features inside of the stack class.
# So, below is adjusted class

import sys

class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		if len(self.items) == 0:
			return 1
		return 0
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		if len(self.items) == 0:
			return -1
		return self.items.pop()
		
	def peek(self):
		if len(self.items) == 0:
			return -1
		return self.items[-1]
	
	def size(self):
		return len(self.items)

stack = Stack()
number_of_orders = int(sys.stdin.readline().rstrip("\n"))
for i in range(number_of_orders):
    order = sys.stdin.readline().rstrip("\n")
    order_buffer = order.split()
    if order_buffer[0] == "push":
        stack.push(int(order_buffer[1]))
    elif order_buffer[0] == "pop":
        print(stack.pop())
    elif order_buffer[0] == "size":
        print(stack.size())
    elif order_buffer[0] == "empty":
        print(stack.isEmpty())
    elif order_buffer[0] == "top":
        print(stack.peek())


