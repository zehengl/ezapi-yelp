from setuptools import setup, find_packages


setup(
    name="ezapi_yelp",
    keywords="Yelp Fusion",
    version="0.4.0",
    packages=find_packages(),
    description="A Python wrapper for Yelp API",
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
