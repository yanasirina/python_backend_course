from os.path import join, dirname
from setuptools import setup, find_packages

setup(
    name='date_utils',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'date_utils', 'README.md')).read(),
)
