import pytest
from data import default_kwargs
from utils import polite


@polite
@pytest.mark.parametrize("kwargs", default_kwargs)
def test_all_categories(yelp_fusion, kwargs):
    """
    test GET /categories

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """

    assert yelp_fusion.all_categories(**kwargs) is not None


@polite
@pytest.mark.parametrize("kwargs", default_kwargs)
def test_category_details(yelp_fusion, kwargs):
    """
    test GET /categories/{alias}

    Args:
        yelp_fusion (yelp.YelpFusion): a YelpFusion object
    """

    assert yelp_fusion.category_details("hotdogs", **kwargs) is not None
