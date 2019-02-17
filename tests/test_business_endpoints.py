import pytest

from .testdata import default_kwargs, loc_lat_long


@pytest.mark.parametrize("kwargs, exception_raised", loc_lat_long)
def test_business_search(yelp_fusion, kwargs, exception_raised):
    """
    test GET /businesses/search

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """
    if exception_raised:
        with pytest.raises(RuntimeError):
            yelp_fusion.business_search(**kwargs)
    else:
        assert yelp_fusion.business_search(**kwargs) is not None


@pytest.mark.parametrize(
    "kwargs, exception_raised", [({}, True), ({"phone": "+14159083801"}, False)]
)
def test_phone_search(yelp_fusion, kwargs, exception_raised):
    """
    test GET /businesses/search/phone

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """
    if exception_raised:
        with pytest.raises(RuntimeError):
            yelp_fusion.phone_search(**kwargs)
    else:
        assert yelp_fusion.phone_search(**kwargs) is not None


@pytest.mark.parametrize("kwargs, exception_raised", loc_lat_long)
def test_transaction_search(yelp_fusion, kwargs, exception_raised):
    """
    test GET /transactions/{transaction_type}/search

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """
    if exception_raised:
        with pytest.raises(RuntimeError):
            yelp_fusion.transaction_search("delivery", **kwargs)
    else:
        assert yelp_fusion.transaction_search("delivery", **kwargs)


@pytest.mark.parametrize("kwargs", default_kwargs)
def test_business_details(yelp_fusion, kwargs):
    """
    test GET /businesses/{id}

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """

    assert yelp_fusion.business_details("WavvLdfdP6g8aZTtbBQHTw", **kwargs) is not None


@pytest.mark.parametrize(
    "kwargs, exception_raised",
    [
        ({}, True),
        ({"name": "Gary Danko"}, True),
        ({"name": "Gary Danko", "address1": "800 N Point St"}, True),
        (
            {
                "name": "Gary Danko",
                "address1": "800 N Point St",
                "city": "San Francisco",
            },
            True,
        ),
        (
            {
                "name": "Gary Danko",
                "address1": "800 N Point St",
                "city": "San Francisco",
                "state": "CA",
            },
            True,
        ),
        (
            {
                "name": "Gary Danko",
                "address1": "800 N Point St",
                "city": "San Francisco",
                "state": "CA",
                "country": "US",
            },
            False,
        ),
    ],
)
def test_business_match(yelp_fusion, kwargs, exception_raised):
    """
    test GET /businesses/matches

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """

    if exception_raised:
        with pytest.raises(RuntimeError):
            yelp_fusion.business_match(**kwargs)
    else:
        assert yelp_fusion.business_match(**kwargs) is not None


@pytest.mark.parametrize("kwargs", default_kwargs)
def test_reviews(yelp_fusion, kwargs):
    """
    test GET /businesses/{id}/reviews

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """

    assert yelp_fusion.reviews("WavvLdfdP6g8aZTtbBQHTw", **kwargs) is not None


@pytest.mark.parametrize(
    "kwargs, exception_raised",
    [
        ({}, True),
        ({"text": "+14159083801"}, False),
        ({"text": "Gary Danko", "latitude": 37.80587, "longitude": -122.42058}, False),
    ],
)
def test_autocomplete(yelp_fusion, kwargs, exception_raised):
    """
    test GET /autocomplete

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """
    if exception_raised:
        with pytest.raises(RuntimeError):
            yelp_fusion.autocomplete(**kwargs)
    else:
        assert yelp_fusion.autocomplete(**kwargs) is not None
