#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'six',
    'Django>=2.0,<2.3',
    'django-model-utils>=3.0,<5.0',
    'django-markupfield>=1.5,<3',
    'django-taggit>=0.22.2,<2.0.0',
    'pillow>=4.0.0,<8.0.0',
]

test_requirements = [
    # None, these go into the test_requirements file
]

setup(
    name='django-andablog',
    version='3.2.0',
    description='A blog app that is only intended to be embedded within an existing Django site.',
    long_description=readme + '\n\n' + history,
    author='Ivan VenOsdel',
    author_email='ivan@wimpyanalytics.com',
    url='https://github.com/WimpyAnalytics/django-andablog',
    download_url='https://github.com/wimpyanalytics/django-andablog/tarball/3.1.0',
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
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Django',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
