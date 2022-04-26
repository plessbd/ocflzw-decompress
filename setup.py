#!/usr/bin/env python

from setuptools import setup, find_packages
import ocflzw_decompress

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ocflzw-decompress',
    version=ocflzw_decompress.VERSION,
    description='OCFLZW Decompress',
    long_description=long_description,
    long_description_content_type="text/markdown",
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