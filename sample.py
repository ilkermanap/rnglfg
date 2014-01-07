import rng 
"""
There are two methods in the rng package:

lfgToFile( size, parameter1, parameter2, file name):
   This method will create a file using Lagged Fibonacci Generator


lfgToList( size, parameter1, parameter2):
   This method will return a list of numbers generated using 
   Lagged Fibonacci Generator

"""


rng.lfgToFile(10000,9739,23209,"test-rng.dat")
x = rng.lfgToList(1000,24,55)
print x
