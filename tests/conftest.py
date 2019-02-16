import os

import pytest

from yelp import YelpFusion


@pytest.fixture(scope="module")
def yelp_fusion():
    token = os.getenv("token", None)

    return YelpFusion(token) if token else None
