#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import projector
version = projector.__version__

setup(
    name='projector',
    version=version,
    author='',
    author_email='matt.warren@gmail.com',
    packages=[
        'projector',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['projector/manage.py'],
)
