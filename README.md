ezapi-yelp
==========

A Python wrapper for Yelp API, supporting [v2](https://www.yelp.com/developers/documentation/v2/overview) and [Fusion](https://www.yelp.com/developers/documentation/v3/get_started) (v3)

* Implement all endpoints
    - **v2**
        * Search
        * Business
        * PhoneSearch
    - **fusion** (v3)
        * Search
        * PhoneSearch
        * TransactionSearch
        * Business
        * Reviews
        * Autocomplete
* Validate all parameters
* Provide CLI
* Include unit tests

# Install
```bash
pip install ezapi_yelp
```

# Test
1. Clone down the repo
    ```bash
    git clone git@github.com:zehengl/ezapi_yelp.git
    cd ezapi_yelp
    ```
2. Create a config file to store your credentials for testing
    ```bash
    touch tests/credentials.conf
    ```
3. Put down your api credentials as follows
    ```
    [v2]
    consumer_key = xxxx
    consumer_secret = xxxx
    token = xxxx
    token_secret = xxxx

    [v3]
    app_id = xxxx
    app_secret = xxxx
    ```
4. Run the tests
    ```bash
    python setup.py test
    ```

# Usage
1. **Python Library**
    To use the python library, please create a Yelp instance with the required credentials.
        
    All parameters are considered as *keyword arguments* (**kwargs).
    
    For **v2** api:
    ```python
    from yelp.api.v2 import Yelp
    
    
    consumer_key = 'xxxx'
    consumer_secret = 'xxxx'
    token = 'xxxx'
    token_secret = 'xxxx'
    
    yelp = Yelp(
        consumer_key, 
        consumer_secret, 
        token, 
        token_secret,
    )
    
    # Simple Examples
    print yelp.search(location='calgary', limit=1)
    print yelp.business('yelp-san-francisco')
    print yelp.phone_search(phone='+14037275451')
    print yelp.search(term='food',bounds='37.900000,-122.500000|37.788022,-122.399797')
    print yelp.search(term='food',ll='37.900000,-122.500000')
    print yelp.search(term='food',location='Hayes',cll='37.77493,-122.419415')
    
    ```
    
    For **fusion** (v3) api:
    ```python
    from yelp.api.v3 import Yelp
    
    
    app_id = 'xxxx'
    app_secret = 'xxxx'
    
    yelp = Yelp(
        app_id,
        app_secret,
    )
    
    # Simple Examples
    print yelp.search(location='calgary', limit=1)
    print yelp.phone_search(phone='+14037275451')
    print yelp.transaction_search('delivery', location='calgary')
    print yelp.business('yelp-san-francisco')
    print yelp.reviews('yelp-san-francisco')
    print yelp.autocomplete(text='pizza', latitude=37.77493, longitude=-122.419415)
    ```

2. **Command Line Interface**
    To use the CLI, please set up the api credentials as environment variables or pass in as options.
        
    All parameters are considered *options* (--PARAMETER=VALUE) in the command line interface.
    
    For **v2** api:
    ```bash
    export consumer_key = xxxx
    export consumer_secret = xxxx
    export token = xxxx
    export token_secret = xxxx
    
    yelp2 business yelp-san-francisco
    yelp2 phone_search --phone=+15555555555
    ```
    
    or
    ```bash
    yelp2 --consumer_key='xxxx' --consumer_secret='xxxx' --token='xxxx' --token_secret='xxxx' ENDPOINT --PARAMETER=yy
    ```
    
    For **fusion** (v3) api:
    ```bash
    export app_id = xxxx
    export app_secret = xxxx
        
    yelp-fusion search --location='san franciso' --limit=10 --indent=2
    yelp-fusion business yelp-san-francisco
    yelp-fusion autocomplete --latitude=37.77493 --longitude=-122.419415 -text='pizza'
    ```
    
    or 
    ```bash
    yelp3 --app_id='xxxx' --app_secret='xxxx' ENDPOINT --PARAMETER=yy
    ```

# Contact

Zeheng Li

imzehengl@gmail.com
