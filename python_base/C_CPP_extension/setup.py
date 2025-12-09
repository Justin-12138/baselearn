from setuptools import setup, Extension

module = Extension(
    "mymath",
    sources=["mymath.c"],
    extra_compile_args=["-fopenmp"],
    extra_link_args=["-fopenmp"],
)

setup(
    name="mymath",
    version="1.0",
    ext_modules=[module],
)
