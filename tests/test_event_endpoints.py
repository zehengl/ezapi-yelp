import pytest

from .testdata import default_kwargs, loc_lat_long


@pytest.mark.parametrize("kwargs", default_kwargs)
def test_event_lookup(yelp_fusion, kwargs):
    """
    test GET /events/{id}

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """

    assert (
        yelp_fusion.event_lookup("oakland-saucy-oakland-restaurant-pop-up", **kwargs)
        is not None
    )


@pytest.mark.parametrize("kwargs", default_kwargs)
def test_event_search(yelp_fusion, kwargs):
    """
    test GET /events

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """

    assert yelp_fusion.event_search(**kwargs) is not None


@pytest.mark.parametrize("kwargs, exception_raised", loc_lat_long)
def test_featured_event(yelp_fusion, kwargs, exception_raised):
    """
    test GET /events/featured

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """
    if exception_raised:
        with pytest.raises(RuntimeError):
            yelp_fusion.featured_event(**kwargs)
    else:
        assert yelp_fusion.featured_event(**kwargs) is not None
