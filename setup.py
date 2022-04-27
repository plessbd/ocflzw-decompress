#!/usr/bin/env python

from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ocflzw-decompress',
    version="1.0.0",
    description='OCFLZW Decompress',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plessbd/ocflzw-decompress",
    project_urls={
        "Bug Tracker": "https://github.com/plessbd/ocflzw-decompress/issues",
    },
    keywords='lzw ocfblob decompress cerner',
    author='Ben Plessinger, Mohammad Zia',
    license='GNU General Public License v3 (GPLv3)',
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data = True,
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)