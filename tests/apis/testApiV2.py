import unittest

from tests import credential_v2, is_error
from yelp.api.v2 import Yelp
from yelp.exceptions import InvalidParameter


class TestYelpV2(unittest.TestCase):

    def setUp(self):
        self.yelp_obj = Yelp(
            credential_v2.get('consumer_key'),
            credential_v2.get('consumer_secret'),
            credential_v2.get('token'),
            credential_v2.get('token_secret'),
        )

    def testSearch_term_location(self):
        resp = self.yelp_obj.search(
            term='food',
            location='san francisco',
        )
        self.assertFalse(is_error(resp))

    def testSearch_term_location_cll(self):
        resp = self.yelp_obj.search(
            term='food',
            location='san francisco',
            cll='37.77493,-122.419415',
        )
        self.assertFalse(is_error(resp))

    def testSearch_term_bounds_limit(self):
        resp = self.yelp_obj.search(
            term='food',
            bounds='37.900000,-122.500000|37.788022,-122.399797',
            limit=3,
        )
        self.assertFalse(is_error(resp))

    def testSearch_term_ll(self):
        resp = self.yelp_obj.search(
            term='food',
            ll='37.77493,-122.419415',
        )
        self.assertFalse(is_error(resp))

    def testSearch_location_limit(self):
        resp = self.yelp_obj.search(
            location='calgary',
            limit=1,
        )
        self.assertFalse(is_error(resp))

    def testSearch_nonexistent_parameter(self):
        self.assertRaises(
            InvalidParameter,
            self.yelp_obj.search,
            locations='calgary',
        )

    def testSearch_invalid_cc(self):
        self.assertRaises(
            InvalidParameter,
            self.yelp_obj.search,
            cc='xxx',
        )

    def testBusiness(self):
        business_id = 'thi-thi-vietnamese-subs-calgary'
        resp = self.yelp_obj.business(business_id)
        self.assertFalse(is_error(resp))

    def testBusiness_actionlinks(self):
        business_id = 'urban-curry-san-francisco'
        resp = self.yelp_obj.business(
            business_id,
            actionlinks=True,
        )
        self.assertFalse(is_error(resp))

    def testBusiness_cc(self):
        business_id = 'thi-thi-vietnamese-subs-calgary'
        resp = self.yelp_obj.business(business_id, cc='ca')
        self.assertFalse(is_error(resp))

    def testPhoneSearch_phone(self):
        resp = self.yelp_obj.phone_search(phone='+15555555555')
        self.assertFalse(is_error(resp))

    def testPhoneSearch_phone_cc_category(self):
        resp = self.yelp_obj.phone_search(
            phone='+15555555555',
            cc='us',
            category='fashion',
        )
        self.assertFalse(is_error(resp))

    def testSearchFail(self):
        resp = self.yelp_obj.search()
        self.assertTrue(is_error(resp))

    def testBusinessFail(self):
        resp = self.yelp_obj.business(business_id='')
        self.assertTrue(is_error(resp))

    def testPhoneSearchFail(self):
        resp = self.yelp_obj.phone_search()
        self.assertTrue(is_error(resp))
