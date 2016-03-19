#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os
import re

from setuptools import setup


def get_version_from_init():
    file = open(os.path.join(os.path.dirname(__file__), 'meta_parser', '__init__.py'))

    regexp = re.compile(r".*__version__ = '(.*?)'", re.S)
    version = regexp.match(file.read()).group(1)
    file.close()

    return version


setup(
    name='meta_parser',
    license='MIT',
    author='Dmitry Merkurev',
    author_email='didika914@gmail.com',
    version=get_version_from_init(),
    url='https://github.com/dimorinny/meta-parser',
    packages=[
        'meta_parser'
    ],
    package_dir={'meta_parser': 'meta_parser'},
    install_requires=[
        'requests',
        'bs4',
        'lxml'
    ]
)