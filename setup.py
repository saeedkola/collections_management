# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in demo/__init__.py
from collections_management import __version__ as version

setup(
	name='collections_management',
	version=version,
	description='This App Helps you track down your Collections',
	author='Element Labs',
	author_email='saeed@elementlabs.xyz',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)