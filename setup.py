#from distutils.core import setup, Extension
 
import setuptools


with open("README.md", "r") as fh:
        long_description = fh.read()

rngmodule = setuptools.Extension('rnglfg', sources = ['rngmodule.c'])
 
setuptools.setup ( name = 'rnglfg',
                   version = '0.2',
                   description = 'Random Number Generator with Lagged Fiboniacci Generator',
                   author = 'Ilker Manap',
                   author_email='ilkermanap@gmail.com',
                   ext_modules = [rngmodule],
                   long_description = long_description,
                   long_description_content_type="text/markdown",
                   url="https://github.com/ilkermanap/lfg",
                   packages=setuptools.find_packages(),
                   classifiers=[

                           "Programming Language :: Python :: 3",
                           "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                           "Operating System :: OS Independent",
                   ],
                   
)
