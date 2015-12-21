# ezapi_yelp
[![PyPI](https://img.shields.io/pypi/dm/ezapi-yelp.svg)](https://pypi.python.org/pypi/ezapi-yelp) [![PyPI](https://img.shields.io/pypi/v/ezapi_yelp.svg)](https://pypi.python.org/pypi/ezapi-yelp)

An easy api for Yelp written in Python

It implements the "search", "business", and "phone_search" api provided by Yelp. For details, see https://www.yelp.com/developers/documentation/v2/overview

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

print test_api.search(location='calgary', limit=1)
print test_api.business('yelp-san-francisco')
print test_api.phone_search(phone='+14037275451')
```

