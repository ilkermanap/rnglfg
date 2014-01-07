from distutils.core import setup, Extension
 
module1 = Extension('rng', sources = ['rngmodule.c'])
 
setup (name = 'PackageName',
        version = '1.0',
        description = 'Random Number Generators',
        ext_modules = [module1])
