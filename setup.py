from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ezapi_yelp',
    keywords='Yelp v2 v3 Fusion',
    version='0.3.0',
    packages=find_packages(exclude=['tests', 'tests.*']),

    description='A Python wrapper for Yelp API',
    long_description=long_description,

    url='https://github.com/zehengl/ezapi-yelp',

    author='Zeheng Li',
    author_email='imzehengl@gmail.com',

    license='MIT',

    entry_points={
        'console_scripts': [
            'yelp2 = yelp.cli.v2:run',
            'yelp3 = yelp.cli.v3:run',
            'yelp-fusion = yelp.cli.v3:run',
        ]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    install_requires=[
        'click',
        'iso3166',
        'iso639',
        'requests_oauthlib',
    ],

    test_suite="tests",
)
