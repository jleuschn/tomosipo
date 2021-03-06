#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.org') as readme_file:
    readme = readme_file.read()

# with open('HISTORY.rst') as history_file:
#     history = history_file.read()

requirements = [
    'pyqtgraph',
    'pyqt5',
    'astra-toolbox',
    'pyopengl',
    'numpy',
]

setup_requirements = []

test_requirements = []

setup(
    author="Allard Hendriksen",
    author_email='allard.hendriksen@cwi.nl',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A usable Python astra-based tomography library.",
    install_requires=requirements,
    license="GPL",
    long_description=readme,
    include_package_data=True,
    keywords='tomography',
    name='tomosipo',
    packages=find_packages(include=['tomosipo']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ahendriksen/tomosipo',
    version='0.0.1',
    zip_safe=False,
)
