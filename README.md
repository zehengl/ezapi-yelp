# ezapi-yelp

A Python wrapper for [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3/get_started),

[![Travis](https://img.shields.io/travis/zehengl/ezapi-yelp.svg)](https://travis-ci.org/zehengl/ezapi-yelp)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![PyPI - License](https://img.shields.io/pypi/l/ezapi-yelp.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ezapi-yelp.svg)
[![PyPI](https://img.shields.io/pypi/v/ezapi-yelp.svg)](https://pypi.python.org/pypi/ezapi-yelp)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/zehengl/ezapi-yelp/0.4.2.svg)

## Install

    pip install ezapi-yelp

## Test

    git clone git@github.com:zehengl/ezapi-yelp.git
    export token="..."
    cd ezapi-yelp
    python setup.py test

## Usage

    from yelp import YelpFusion

    token = "..."

    yelp_fusion = YelpFusion(token)

    print(yelp_fusion.business_search(location="San Francisco"))
    print(yelp_fusion.transaction_search("delivery", location="San Francisco"))
    print(yelp_fusion.business_details("WavvLdfdP6g8aZTtbBQHTw"))
    print(
        yelp_fusion.business_match(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )
    )
    print(yelp_fusion.reviews("WavvLdfdP6g8aZTtbBQHTw"))
    print(
        yelp_fusion.autocomplete(
            text="Gary Danko", latitude=37.80587, longitude=-122.42058
        )
    )
    print(yelp_fusion.all_categories())
    print(yelp_fusion.category_details("hotdogs"))
    print(yelp_fusion.event_lookup("oakland-saucy-oakland-restaurant-pop-up"))
    print(yelp_fusion.event_search(location="Oakland"))
    print(yelp_fusion.featured_event(location="Oakland"))
