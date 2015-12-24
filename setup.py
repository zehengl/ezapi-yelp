
from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ezapi_yelp',

    version='0.2.0',

    description='An easy api for Yelp written in Python',
    long_description=long_description,

    url='https://github.com/zehengl/ezapi_yelp',

    author='Zeheng Li',
    author_email='imzehengl@gmail.com',

    license='MIT',

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

    packages=[
        'ezapi_yelp',
    ],

    keywords='Yelp API',

    install_requires=['requests_oauthlib'],

)