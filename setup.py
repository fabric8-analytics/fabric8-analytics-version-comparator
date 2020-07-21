#!/usr/bin/env python3

"""Project setup file for the analytics server project."""

from setuptools import setup, find_packages


# There are not specific dependencies for this component, except python 3.6
reqs, dep_links = [], []

setup(
    name='f8a_version_comparator',
    version='0.1',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=reqs,
    dependency_links=dep_links,
    include_package_data=True,
    author='Geetika Batra',
    author_email='gbatra@redhat.com',
    description='fabric8-analytics maven version comparator',
    license='ASL 2.0',
    keywords='fabric8 analytics Maven Version Comparator',
    url='https://github.com/fabric8-analytics/fabric8-analytics-version-comparator'
)
