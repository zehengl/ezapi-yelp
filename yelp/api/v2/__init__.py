from requests_oauthlib import OAuth1Session

import yelp.api
from yelp import utils


base_path = '/v2'


class Endpoints:
    Search = '/search'
    Business = '/business/%s'
    PhoneSearch = '/phone_search'


params_validation = {
    Endpoints.Search: {
        'term': lambda term: isinstance(term, str),
        'limit': lambda limit: isinstance(limit, int),
        'offset': lambda offset: isinstance(offset, int),
        'sort': lambda sort: isinstance(sort, int),
        'category_filter': lambda category_filter: isinstance(category_filter, str),
        'radius_filter': lambda radius_filter: isinstance(radius_filter, str),
        'deals_filter': lambda deals_filter: isinstance(deals_filter, bool),

        'location': lambda location: isinstance(location, str),
        'cll': lambda cll: isinstance(cll, str) and utils.is_valid_cll(cll),
        'bounds': lambda bounds: isinstance(bounds, str) and utils.is_valid_bounds(bounds),
        'll': lambda ll: isinstance(ll, str) and utils.is_valid_ll(ll),

        'cc': lambda cc: isinstance(cc, str) and utils.is_valid_cc(cc),
        'lang': lambda lang: isinstance(lang, str) and utils.is_valid_lang(lang),

        'actionlinks': lambda actionlinks: isinstance(actionlinks, bool),
    },

    Endpoints.Business: {
        'cc': lambda cc: isinstance(cc, str) and utils.is_valid_cc(cc),
        'lang': lambda lang: isinstance(lang, str) and utils.is_valid_lang(lang),

        'actionlinks': lambda actionlinks: isinstance(actionlinks, bool),
    },

    Endpoints.PhoneSearch: {
        'phone': lambda phone: isinstance(phone, str),
        'cc': lambda cc: isinstance(cc, str) and utils.is_valid_cc(cc),
        'category': lambda category: isinstance(category, str),
    },
}


class Yelp:
    def __init__(self, consumer_key, consumer_secret, token, token_secret):
        self.session = OAuth1Session(
            consumer_key,
            consumer_secret,
            token,
            token_secret
        )

    @staticmethod
    def _search_url():
        return utils.make_url(yelp.api.host, base_path, Endpoints.Search)

    @staticmethod
    def _business_url(business_id):
        return utils.make_url(yelp.api.host, base_path, Endpoints.Business % business_id)

    @staticmethod
    def _phone_search_url():
        return utils.make_url(yelp.api.host, base_path, Endpoints.PhoneSearch)

    @utils.validate(params_validation, Endpoints.Search)
    def search(self, **kwargs):
        return self.session.get(self._search_url(), params=kwargs).json()

    @utils.validate(params_validation, Endpoints.Business)
    def business(self, business_id, **kwargs):
        return self.session.get(self._business_url(business_id), params=kwargs).json()

    @utils.validate(params_validation, Endpoints.PhoneSearch)
    def phone_search(self, **kwargs):
        return self.session.get(self._phone_search_url(), params=kwargs).json()
