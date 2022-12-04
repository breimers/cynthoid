from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    ext_modules=cythonize(
        ["src/waves.py", "src/notes.py", "src/input.py"],
        compiler_directives={'language_level' : "3"}
    ),
    zip_safe=False,
)
