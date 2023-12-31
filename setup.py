from setuptools import setup, Extension
import sys, numpy
from Cython.Build import cythonize

# Find all includes
local_inc = 'src/pyearth'
numpy_inc = numpy.get_include()

compiler_directives = {"language_level": 3, "embedsignature": True}
define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]

# Set up the ext_modules for Cython, assuming Cython is used
ext_modules = cythonize([
    Extension("pyearth._util", ["src/pyearth/_util.pyx"], 
        include_dirs=[local_inc, numpy_inc],
        define_macros = define_macros,),
    Extension("pyearth._basis",["src/pyearth/_basis.pyx"], 
        include_dirs=[local_inc, numpy_inc],
        define_macros = define_macros,),
    Extension("pyearth._types",["src/pyearth/_types.pyx"],
        include_dirs=[local_inc,numpy_inc],
        define_macros = define_macros,),
    Extension("pyearth._qr",["src/pyearth/_qr.pyx"],
        include_dirs=[local_inc,numpy_inc],
        define_macros = define_macros,),
    Extension("pyearth._knot_search",["src/pyearth/_knot_search.pyx"],
        include_dirs=[local_inc,numpy_inc],
        define_macros = define_macros,),
    Extension("pyearth._record",["src/pyearth/_record.pyx"],
        include_dirs=[local_inc,numpy_inc],
        define_macros = define_macros,),
    Extension("pyearth._forward",["src/pyearth/_forward.pyx"],
        include_dirs=[local_inc,numpy_inc],
        define_macros = define_macros,),
     Extension("pyearth._pruning",["src/pyearth/_pruning.pyx"],
        include_dirs=[local_inc,numpy_inc],
        define_macros = define_macros,),
    ],
    compiler_directives = compiler_directives)

setup(
    ext_modules = ext_modules
)
