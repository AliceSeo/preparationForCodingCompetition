# Basic way to print out strings in a particular format. 
# Usually it is required to solve questions for coding competitions.

# Syntax
print("string_containing_curly_braces".format(element1, element2, element3))
# In this case, string_contatining_curly_braces should contain 3 curly braces.
# For example,

name = "Alice"
age = 20
school = "University of New Zealand"
gender = "F"
print("Name:{}, Age:{}, School:{}, Genger:{}".format(name, age, school, gender))

# will give
>> Name:Alice, Age:20, School:University of New Zealand, Genger:F
# as the output
# by using this, we can print out large size data in a particular given format

# Also, sometimes, it is not allowed to use print() in coding competition 
# In that case, we can use sys.stdout.write()
# Note this does not contain new line character at the end unlike print(). So, we need to mannually add it like this:

import sys
sys.stdout.write("Hello world!\n")

# Another important point is it does not automatically convert other types into printable form (ie. string) 
# hence, it needs to be converted mannually by using str()

big_number = 111111
sys.stdout.write(str(big_number))


