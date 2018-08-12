#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='clicktool',
    use_scm_version={'write_to': 'src/clicktool/__version__.py'},
    setup_requires=['setuptools_scm'],
    packages=find_packages('src'),
    install_requires=[
        'Click',
    ],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'clicktool=clicktool.cli:cli'
        ]
    }
)
