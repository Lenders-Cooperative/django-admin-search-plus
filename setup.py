#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages

import admin_search_plus

readme = open("README.md").read()

setup(
    name="admin-search-plus",
    version=admin_search_plus.__version__,
    author=admin_search_plus.__author__,
    description="Mixin for Django's admin objects to enhance searching",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="dgraves@gravitate-us.com",
    url="https://github.com/Lenders-Cooperative/admin-search-plus",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=3.6",
    ],
    keywords="django admin search",
    license="MIT",
    platforms=["any"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)