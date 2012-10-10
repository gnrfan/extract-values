#!/usr/bin/env python

import os
from distutils.core import setup

version = '1.0'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.1",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
]

root_dir = os.path.dirname(__file__)
if not root_dir:
    root_dir = '.'
long_desc = open(root_dir + '/README.md').read()

setup(
    name='extract-values',
    version=version,
    url='https://github.com/gnrfan/extract-values',
    download_url='https://github.com/gnrfan/extract-values/zipball/master',
    author='Antonio Ognio',
    author_email='antonio@ognio.com',
    license='BSD License',
    py_modules=['extract_values'],
    description='A Python module for extracting values out of a string '
                'using a simple pattern instead of a regular expression.',
    classifiers=classifiers,
    long_description=long_desc,
)
