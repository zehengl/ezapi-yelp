import os
import sys

import pytest
from dotenv import load_dotenv

from yelp import YelpFusion

sys.path.append(os.path.join(os.path.dirname(__file__), "helpers"))
load_dotenv()


@pytest.fixture(scope="module")
def yelp_fusion():
    token = os.getenv("yelp_token", None)

    return YelpFusion(token) if token else None
