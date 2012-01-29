#!./venv/bin/python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
import sys

if __name__ == '__main__':
    setup(name='tklive',
        version='0.1',
        description="",
        author='Dominik "Socek" Długajczyk',
        author_email='msocek@gmail.com',
        license='?',
        packages=find_packages(),
        install_requires=["django==1.3.1", "south", 'ipdb']
    )
