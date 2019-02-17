from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name="ezapi_yelp",
    keywords="Yelp Fusion",
    version="0.4.1",
    packages=find_packages(),
    description="A Python wrapper for Yelp API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zehengl/ezapi-yelp",
    author="Zeheng Li",
    author_email="imzehengl@gmail.com",
    maintainer="Zeheng Li",
    maintainer_email="imzehengl@gmail.com",
    license="MIT",
    install_requires=["requests", "wrapt"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
