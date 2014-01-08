from distutils.core import setup, Extension
 
rngmodule = Extension('rng', sources = ['rngmodule.c'])
 
setup ( name = 'rng',
        version = '1.0',
        description = 'Random Number Generators',
        author = 'Ilker Manap',
        author_email='ilkermanap@gmail.com',
        ext_modules = [rngmodule])
