import unittest

from tests import credential_v3, is_error
from yelp.api.v3 import Yelp
from yelp.exceptions import InvalidParameter, InvalidTransactionType


class TestYelpV3(unittest.TestCase):

    def setUp(self):
        self.yelp_obj = Yelp(
            credential_v3.get('app_id'),
            credential_v3.get('app_secret'),
        )

    def testSearch_location_limit(self):
        resp = self.yelp_obj.search(
            location='calgary',
            limit=1,
        )
        self.assertFalse(is_error(resp))

    def testSearch_term_location(self):
        resp = self.yelp_obj.search(
            term='food',
            location='san francisco',
        )
        self.assertFalse(is_error(resp))

    def testSearch_term_location_lat_long(self):
        resp = self.yelp_obj.search(
            term='food',
            location='san francisco',
            latitude=37.77493,
            longitude=-122.419415,
        )
        self.assertFalse(is_error(resp))

    def testSearch_location_limit_open_now(self):
        resp = self.yelp_obj.search(
            location='calgary',
            limit=10,
            open_now=True,
        )
        self.assertFalse(is_error(resp))

    def testPhoneSearch_phone(self):
        resp = self.yelp_obj.phone_search(
            phone='+15555555555',
        )
        self.assertFalse(is_error(resp))

    def testTransactionSearch_location(self):
        resp = self.yelp_obj.transaction_search(
            'delivery',
            location='calgary',
        )
        self.assertFalse(is_error(resp))

    def testTransactionSearch_lat_long(self):
        resp = self.yelp_obj.transaction_search(
            'delivery',
            latitude=37.77493,
            longitude=-122.419415,
        )
        self.assertFalse(is_error(resp))

    def testBusiness(self):
        business_id = 'thi-thi-vietnamese-subs-calgary'
        resp = self.yelp_obj.business(business_id)
        self.assertFalse(is_error(resp))

    def testReviews(self):
        business_id = 'thi-thi-vietnamese-subs-calgary'
        resp = self.yelp_obj.reviews(business_id)
        self.assertFalse(is_error(resp))

    def testAutocomplete_text(self):
        resp = self.yelp_obj.autocomplete(
            text='Delivery'
        )
        self.assertFalse(is_error(resp))

    def testAutocomplete_text_lat_long(self):
        resp = self.yelp_obj.autocomplete(
            text='pizza',
            latitude=37.77493,
            longitude=-122.419415,
        )
        self.assertFalse(is_error(resp))

    def testAutocomplete_text_locale(self):
        resp = self.yelp_obj.autocomplete(
            text='pizza',
            locale='en_CA',
        )
        self.assertFalse(is_error(resp))

    def testSearchFail(self):
        resp = self.yelp_obj.search()
        self.assertTrue(is_error(resp))

    def testPhoneSearchFail(self):
        resp = self.yelp_obj.phone_search()
        self.assertTrue(is_error(resp))

    def testTransactionSearchFail(self):
        resp = self.yelp_obj.transaction_search(
            'delivery'
        )
        self.assertTrue(is_error(resp))

    def testTransactionSearchInvalidTransactionType(self):
        self.assertRaises(
            InvalidTransactionType,
            self.yelp_obj.transaction_search,
            'notype',
            latitude=37.77493,
            longitude=-122.419415,
        )

    def testBusinessInvalidParameter(self):
        business_id = 'urban-curry-san-francisco'
        self.assertRaises(
            InvalidParameter,
            self.yelp_obj.business,
            business_id,
            actionlinks=True,
        )
