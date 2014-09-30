#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'Django',
    'South',  # For 1.6.6 compatibility
]

test_requirements = [
    # None, these go into a requirements file
]

setup(
    name='django-andablog',
    version='0.1.0',
    description='A blog app that is intended to embed within an existing Django site.',
    long_description=readme + '\n\n' + history,
    author='Ivan Ven Osdel',
    author_email='ivan@wimpyanalytics.com',
    url='https://github.com/WimpyAnalytics/django-andablog',
    packages=[
        'djangoandablog',
    ],
    package_dir={'djangoandablog':
                 'djangoandablog'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='django-andablog',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
