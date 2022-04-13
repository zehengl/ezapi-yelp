import os

import pytest
from dotenv import load_dotenv
from yelp import YelpFusion

load_dotenv()


@pytest.fixture(scope="module")
def yelp_fusion():
    token = os.getenv("token", None)

    return YelpFusion(token) if token else None
