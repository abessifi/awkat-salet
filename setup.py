#!/usr/bin/env python

"""
Setup script for awkat_salet.
"""

import setuptools

from awkat_salet import __project__, __version__

import os
if os.path.exists('README.md'):
    README = open('README.md').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name=__project__,
    version=__version__,

    description="Awkat-Salet is a Python Prayer reminder program.",
    url='https://github.com/abessifi/awkat-salet',
    author='Ahmed Bessifi',
    author_email='ahmed.bessifi@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=(README + '\n' + CHANGES),
    license='GPLv3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: GNU/Linux',
        'Programming Language :: Python :: 2.7',
    ],

    install_requires=open('requirements').readlines(),
)
