import unittest

import yelp


class TestYelpUtils(unittest.TestCase):

    def testIsAllFloat(self):
        self.assertTrue(
            yelp.utils._is_all_float([
                '0'
                '1',
                '2',
                '3',
            ])
        )
        self.assertTrue(
            yelp.utils._is_all_float([
                '0.0',
                '1.1',
                '2.2',
                '3.3',
            ])
        )
        self.assertFalse(
            yelp.utils._is_all_float([
                '1.1',
                '2.2a',
                '3.3',
            ])
        )

    def testIsValid_cll(self):
        self.assertTrue(
            yelp.utils.is_valid_cll('37.77493,-122.419415')
        )
        self.assertFalse(
            yelp.utils.is_valid_cll('37.77493,-122.419415,123')
        )
        self.assertFalse(
            yelp.utils.is_valid_cll('abc,-122.419415')
        )
        self.assertFalse(
            yelp.utils.is_valid_cll('37.77493,')
        )
        self.assertFalse(
            yelp.utils.is_valid_cll(',-122.419415')
        )

    def testIsValid_ll(self):
        self.assertTrue(
            yelp.utils.is_valid_ll('37.77493,-122.419415')
        )
        self.assertTrue(
            yelp.utils.is_valid_ll('37.77493,-122.419415,.99')
        )
        self.assertTrue(
            yelp.utils.is_valid_ll('37.77493,-122.419415,.99,123')
        )
        self.assertTrue(
            yelp.utils.is_valid_ll('37.77493,-122.419415,.99,123,.88')
        )

        self.assertFalse(
            yelp.utils.is_valid_ll('abc,-122.419415')
        )
        self.assertFalse(
            yelp.utils.is_valid_ll('37.77493,')
        )
        self.assertFalse(
            yelp.utils.is_valid_ll(',-122.419415')
        )

    def testIsValid_bounds(self):
        self.assertTrue(
            yelp.utils.is_valid_bounds('37.900000,-122.500000|37.788022,-122.399797')
        )
        self.assertFalse(
            yelp.utils.is_valid_bounds('37.900000,|,-122.399797')
        )
        self.assertFalse(
            yelp.utils.is_valid_bounds('abc,-122.500000|37.788022,edf')
        )

    def testIsValid_cc(self):
        self.assertTrue(
            yelp.utils.is_valid_cc('us')
        )
        self.assertFalse(
            yelp.utils.is_valid_cc('xx')
        )

    def testIsValid_lang(self):
        self.assertTrue(
            yelp.utils.is_valid_lang('en')
        )
        self.assertTrue(
            yelp.utils.is_valid_lang('fil')
        )
        self.assertFalse(
            yelp.utils.is_valid_lang('xx')
        )
        self.assertFalse(
            yelp.utils.is_valid_lang('xxx')
        )

    def testIsValid_locale(self):
        self.assertTrue(
            yelp.utils.is_valid_locale('cs_CZ')
        )
        self.assertTrue(
            yelp.utils.is_valid_locale('en_CA')
        )
        self.assertFalse(
            yelp.utils.is_valid_locale('xx_CA')
        )
        self.assertFalse(
            yelp.utils.is_valid_locale('en_xxx')
        )

    def testMake_url(self):
        self.assertTrue(
            yelp.utils.make_url('a', 'b') == 'ab'
        )
        self.assertTrue(
            yelp.utils.make_url('a', 'b', 'c') == 'abc'
        )
