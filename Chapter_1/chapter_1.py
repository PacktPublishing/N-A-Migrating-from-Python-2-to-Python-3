# Migrating from Python 2 to Python 3 
# Examples of Chapter 1

# THe next code gets an error in Python 2
# (If you try with the GUI, this error was fixed at the lastest versions)

print 'Spain in Spanish is written España'

# In Python 3, dont gets a error

print('Spain in Spanish is written España')

#
# Print is a function:
#

# Python 2:

print "hello world"

# Python 3

print("hello world")

#
# Divisions:
#

# In Python 2 

1/2 # returns 1
1/2.0 # return 0.5

# In Python 3

1/2 #return 0.5
4/2 #return 2.0

#
# Input:
#

# In Python 2:

my_input=input("Introduce anything: ") 
type(my_input) # return <type 'int'>

my_input=raw_input("Introduce anything: ")
type(my_input) # return <type 'str'>

# In Python 3:

my_input=input("Introduce anything: ")
type(my_input) #return <class 'str'>

#
# Next is a function
#

# In Python 2:

x = iter([1, 2, 3])
x.next() # is valid
next(x) # is valid

# In Python 3:

x = iter([1, 2, 3])
x.next() # NOT is valid
next(x) # is valid

#
# Differences in type comparison
#

# In Python 2:

(1,2)>[1,2] # return True
[1,2,3,4,5] > "hey" # return False
"Hey" > 0 # return True

# In Python 3:

(1,2)>[1,2] # gets errror
[1,2,3,4,5] > "hey" # gets errror
"Hey" > 0 # gets errror

#
#Exceptions
#

# In Python 2:

raise IOError, "activate file exception" # is correct
raise IOError("activate file exception") # is correct

# In Python 3:

raise IOError, "activate file exception" # gets errror
raise IOError("activate file exception") # is correct

#
# news in Python 3.0
#

# new unicode identifiers:
España=True
π = math.pi

# Keyword-Only Arguments

def f(a,*b,c):
 return a+len(b)+c

f(1,c=2) # return 3
f(1,2,c=2) # return 4

# Advanced unpacking
 
 a, b, *rest = range(10)
 
#
# news in Python 3.1
#

# Format function

format(1234567, ',d') # return '1,234,567'
format(1234567.89, ',.2f') # return '1,234,567.89'

# with statement

with open('my_file.txt') as infile, open('a.out', 'w') as outfile:
     for line in infile:
         if '<critical>' in line:
             outfile.write(line)
			 
#
# news in Python 3.2
#		

# New module argparse

import argparse
parser = argparse.ArgumentParser() 
parser.add_argument('action',choices = ['curl'])
parser.add_argument('-m',required = False)
parser.add_argument('targets',metavar = 'HOSTNAME',nargs = '+') 

cmd = 'curl -m 10 pythonconverter.com'
result = parser.parse_args(cmd.split())
result.action # return 'curl'
result.targets # return ['pythonconverter.com']
result.m # return '10'

#
# news in Python 3.3
#	

# yield from

def g(x):
 yield from range(x, 0, -1)
 yield from range(x, 10, 1)
print(list(g(5))) # return [5, 4, 3, 2, 1, 5, 6, 7, 8, 9]

# Managing the IP address

import ipaddress
ipaddress.ip_address('192.168.0.1') # return IPv4Address('192.168.0.1')

#
# news in Python 3.5
#	

# New operator for matrix multiplication: @

import numpy
x = numpy.ones(3)
x # return array([ 1., 1., 1.])
m = numpy.eye(3)
m # return 
#array([[ 1., 0., 0.],
#[ 0., 1., 0.],
#[ 0., 0., 1.]])

x @ m # return 
array([ 1., 1., 1.])

# Additional Unpacking Generalizations

print(*[1], *[2], 3) # return 1 2 3

dict(**{'x': 1}, y=2, **{'z': 3}) # return {'x': 1, 'y': 2, 'z': 3}

#
# news in Python 3.6
#	

1_000_000 # return 1000000

version = "3"
f"Python {version}" # return 'Python 3'
