from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

import yelp.api
from yelp.exceptions import InvalidTransactionType


base_path = '/v3'
transaction_types = (
    'delivery',
)


class Endpoints:
    Token = '/oauth2/token'
    Search = '/businesses/search'
    PhoneSearch = '/businesses/search/phone'
    TransactionSearch = '/transactions/%s/search'
    Business = '/businesses/%s'
    Reviews = '/businesses/%s/reviews'
    Autocomplete = '/autocomplete'


params_validation = {
    Endpoints.Search: {
        'term': lambda term: isinstance(term, str),
        'location': lambda location: isinstance(location, str),
        'latitude': lambda latitude: isinstance(latitude, float),
        'longitude': lambda longitude: isinstance(longitude, float),
        'radius': lambda radius: isinstance(radius, int),
        'categories': lambda categories: isinstance(categories, str),
        'locale': lambda locale: isinstance(locale, str) and yelp.api.utils.is_valid_locale(locale),
        'limit': lambda limit: isinstance(limit, int),
        'offset': lambda offset: isinstance(offset, int),
        'sort_by': lambda sort_by: isinstance(sort_by, str),
        'price': lambda price: isinstance(price, str),
        'open_now': lambda open_now: isinstance(open_now, bool),
        'open_at': lambda open_at: isinstance(open_at, int),
        'attributes': lambda attributes: isinstance(attributes, str),
    },

    Endpoints.PhoneSearch: {
        'phone': lambda phone: isinstance(phone, str),
    },

    Endpoints.TransactionSearch: {
        'latitude': lambda latitude: isinstance(latitude, float),
        'longitude': lambda longitude: isinstance(longitude, float),
        'location': lambda location: isinstance(location, str),
    },

    Endpoints.Business: {
    },

    Endpoints.Reviews: {
        'locale': lambda locale: isinstance(locale, str) and yelp.api.utils.is_valid_locale(locale),
    },

    Endpoints.Autocomplete: {
        'text': lambda text: isinstance(text, str),
        'latitude': lambda latitude: isinstance(latitude, float),
        'longitude': lambda longitude: isinstance(longitude, float),
        'locale': lambda locale: isinstance(locale, str) and yelp.api.utils.is_valid_locale(locale),
    },
}


class Yelp:
    def __init__(self, app_id, app_secret):
        self.session = OAuth2Session(client=BackendApplicationClient(app_id))
        self.session.fetch_token(
            self._token_url(),
            client_id=app_id,
            client_secret=app_secret,
        )

    @staticmethod
    def _token_url():
        return '%s%s' % (yelp.api.host, Endpoints.Token)

    @staticmethod
    def _search_url():
        return '%s%s%s' % (yelp.api.host, base_path, Endpoints.Search)

    @staticmethod
    def _phone_search_url():
        return '%s%s%s' % (yelp.api.host, base_path, Endpoints.PhoneSearch)

    @staticmethod
    def _transaction_search_url(transaction_type):
        if transaction_type not in transaction_types:
            raise InvalidTransactionType(transaction_type)
        return '%s%s%s' % (yelp.api.host, base_path, Endpoints.TransactionSearch % transaction_type)

    @staticmethod
    def _business_url(business_id):
        return '%s%s%s' % (yelp.api.host, base_path, Endpoints.Business % business_id)

    @staticmethod
    def _reviews_url(business_id):
        return '%s%s%s' % (yelp.api.host, base_path, Endpoints.Reviews % business_id)

    @staticmethod
    def _autocomplete_url():
        return '%s%s%s' % (yelp.api.host, base_path, Endpoints.Autocomplete)

    def search(self, **kwargs):
        yelp.utils.validate(params_validation, Endpoints.Search, **kwargs)
        return self.session.get(self._search_url(), params=kwargs).json()

    def phone_search(self, **kwargs):
        yelp.utils.validate(params_validation, Endpoints.PhoneSearch, **kwargs)
        return self.session.get(self._phone_search_url(), params=kwargs).json()

    def transaction_search(self, transaction_type, **kwargs):
        yelp.utils.validate(params_validation, Endpoints.TransactionSearch, **kwargs)
        return self.session.get(self._transaction_search_url(transaction_type), params=kwargs).json()

    def business(self, business_id, **kwargs):
        yelp.utils.validate(params_validation, Endpoints.Business, **kwargs)
        return self.session.get(self._business_url(business_id), params=kwargs).json()

    def reviews(self, business_id, **kwargs):
        yelp.utils.validate(params_validation, Endpoints.Reviews, **kwargs)
        return self.session.get(self._reviews_url(business_id), params=kwargs).json()

    def autocomplete(self, **kwargs):
        yelp.utils.validate(params_validation, Endpoints.Autocomplete, **kwargs)
        return self.session.get(self._autocomplete_url(), params=kwargs).json()
