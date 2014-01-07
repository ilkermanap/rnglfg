lfg
===

Python implementation of Lagged Fibonacci Generator (LFG)

There are two methods:

  lfgToFile(size, param1, param2, filename):

    This method will create a file using random numbers generated with 
    LFG algorithm.

    Method will not return anything.

    size    : File size
    param1  : Lag parameter
    param2  : Size of the seed
    filename: Name of the output file, overwritten if exists.


  lfgToList(size, param1, param2):

    This method will return a list of random numbers generated with 
    LFG algorithm.

    size    : File size
    param1  : Lag parameter
    param2  : Size of the seed
