# ezapi_yelp
[![PyPI](https://img.shields.io/pypi/dm/ezapi-yelp.svg)](https://pypi.python.org/pypi/ezapi-yelp) [![PyPI](https://img.shields.io/pypi/v/ezapi_yelp.svg)](https://pypi.python.org/pypi/ezapi-yelp)

An easy api for Yelp written in Python

It implements the "**search**", "**business**", and "**phone_search**" api provided by Yelp. For details, see https://www.yelp.com/developers/documentation/v2/overview

# Install
```bash
pip install ezapi_yelp
```

# Usage
```python
from ezapi_yelp import EZapiYelp

consumer_key        = 'YOUR consumer_key'
consumer_secret     = 'YOUR consumer_secret'
access_token        = 'YOUR access_token'
access_token_secret = 'YOUR access_token_secret'

test_api = EZapiYelp(consumer_key, consumer_secret, access_token, access_token_secret)

# Simple examples
print test_api.search(location='calgary', limit=1)
print test_api.business('yelp-san-francisco')
print test_api.phone_search(phone='+14037275451')
```

# Changelist
* 2015/12/21
    - instantiate the EZapiYelp with *consumer key*, *consumer secret*, *access token*, and *access token secret*
    - Parameter type checking, raise error if there is a type mismatch
    - "**search**" api
        + 80% Complete
        + **location** is required for search operation, however, only parameter "location" is implemented, "cll" (latitude,longitude) is not done yet
    - "**business**" api
        + Complete
        + lookup business info by id, with optional parameters
    - "**phone_search**" api
        + Complete
        + lookup business info by phone, with optional parameters

# TODO
- complete "**search**" api's search by latitude, longitude functionalities
