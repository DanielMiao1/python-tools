# -*- coding: utf-8 -*-

import setuptools
import sys

if sys.version_info < (2, 7):
	raise ImportError("This library requires Python 2.7 or later.")

setuptools.setup(
	name="python-tools",
	version="v0.0.1.dev0",
	author="Daniel M",
	author_email="danielmiao2019@icloud.com",
	description="A set of tools for python",
	url="https://github.com/DanielMiao1/python-tools",
	classifiers=[
		"Programming Language :: Python 3",
		"Operating System :: OS Independent"
	],
	zip_safe=False,
	packages=["tools"],
	package_dir={"": "."},
	python_requires=">=2.7",
)