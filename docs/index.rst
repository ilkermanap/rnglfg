Welcome to rnglfg's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

rnglfg
======

Python implementation of Lagged Fibonacci Generator (LFG)

Installation
------------

Use pip to install:

.. code-block:: bash
		
   pip3 install rnglfg

Usage
-----

There are two methods:

* lfgToFile(size, param1, param2, filename)
* lfgToList(size, param1, param2)


lfgToFile
*********

lfgToFile(size, param1, param2, filename)

This method will create a file using random numbers generated with 
LFG algorithm.



Method will not return anything.

* size    : File size in bytes. Not count of random numbers to generate. 
* param1  : Lag parameter
* param2  : Size of the seed
* filename: Name of the output file, overwritten if exists.

.. code-block:: python
		
   from rnglfg import lfgToFile
   lfgToFile(100, 24,55, 'randomnumbers.dat')

    
lfgToList
*********

lfgToList(size, param1, param2):

This method will return a list of random numbers generated with 
LFG algorithm.

* size    : Count of random numbers to generate.
* param1  : Lag parameter
* param2  : Size of the seed

.. code-block:: python
		
   from rnglfg import lfgToList
   numbers = lfgToList(100, 24,55)


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
