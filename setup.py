#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'six',
    'Django>=1.7,<1.9',
    'django-model-utils>=2.2',
    'django-markitup>=2.2.2',
    'django-taggit>=0.14.0',
    'pillow>=2.6.1',
]

test_requirements = [
    # None, these go into the test_requirements file
]

setup(
    name='django-andablog',
    version='1.4.0',
    description='A blog app that is only intended to be embedded within an existing Django site.',
    long_description=readme + '\n\n' + history,
    author='Ivan Ven Osdel',
    author_email='ivan@wimpyanalytics.com',
    url='https://github.com/WimpyAnalytics/django-andablog',
    download_url='https://github.com/wimpyanalytics/django-andablog/tarball/1.4.0',
    packages=[
        'andablog',
    ],
    package_dir={'andablog':
                 'andablog'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords=['django-andablog', 'blog', 'django', 'app', 'reusable app', 'andablog'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
