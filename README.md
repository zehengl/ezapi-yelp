<div align="center">
    <img src="https://cdn2.iconfinder.com/data/icons/social-media-applications/64/social_media_applications_28-yelp-512.png" alt="yelp" height="96">
</div>

# ezapi-yelp

[![pytest](https://github.com/zehengl/ezapi-yelp/actions/workflows/pytest.yml/badge.svg)](https://github.com/zehengl/ezapi-yelp/actions/workflows/pytest.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![PyPI - License](https://img.shields.io/pypi/l/ezapi-yelp.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ezapi-yelp.svg)
[![Downloads](https://static.pepy.tech/badge/ezapi-yelp)](https://pepy.tech/project/ezapi-yelp)
[![GitHub Pages](https://github.com/zehengl/ezapi-yelp/actions/workflows/gh-deploy.yml/badge.svg)](https://github.com/zehengl/ezapi-yelp/actions/workflows/gh-deploy.yml)

A Python wrapper for [Yelp Fusion API](https://docs.developer.yelp.com/docs/fusion-intro)

## Install

From [PyPi](https://pypi.org/project/ezapi-yelp/)

    pip install ezapi-yelp

From [GitHub](https://github.com/zehengl/ezapi-yelp)

    pip install git+https://github.com/zehengl/ezapi-yelp.git

## Usage

```python
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
```

## Test

```bash
git clone git@github.com:zehengl/ezapi-yelp.git
cd ezapi-yelp
export yelp_token="..."
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements-test.txt
pytest
```

Use `$Env:yelp_token="..."` to set the api key environment variable on Windows.

## Credits

- [Icon][1] by [tulpahn][2]

[1]: https://www.iconfinder.com/icons/4102600/applications_media_social_yelp_icon
[2]: https://www.iconfinder.com/tulpahn
