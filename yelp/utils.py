from functools import wraps
import re

from iso3166 import countries
from iso639 import is_valid639_1, is_valid639_2
from six import iteritems

from yelp.exceptions import InvalidEndpoint, InvalidParameter


def is_valid_cc(cc):
    try:
        return countries.get(cc) is not None
    except KeyError:
        return False


def is_valid_lang(lang):
    try:
        return is_valid639_1(lang) or is_valid639_2(lang)
    except KeyError:
        return False


def is_valid_locale(locale):
    if len(re.findall(r"_", locale)) != 1:
        return False
    [lang, cc] = locale.split('_')
    return is_valid_lang(lang) and is_valid_cc(cc)


def _is_all_float(parameter_list):
    for p in parameter_list:
        try:
            float(p)
        except ValueError:
            return False
    return True


def is_valid_cll(cll):
    cll_parameters = cll.split(',')
    if len(cll_parameters) != 2:
        return False
    return _is_all_float(cll_parameters)


def is_valid_ll(ll):
    ll_parameters = ll.split(',')
    if len(ll_parameters) not in range(2, 6):
        return False
    return _is_all_float(ll_parameters)


def is_valid_bounds(bounds):
    if len(re.findall(r"\|", bounds)) != 1:
        return False
    for parts in bounds.split('|'):
        if not is_valid_cll(parts):
            return False
    return True


def validate(parameter_validation, endpoint):
    def _validate(parameter_validation, endpoint, **kwargs):
        if endpoint not in parameter_validation:
            raise InvalidEndpoint

        for (k, v) in iteritems(kwargs):
            _is_validate_func = parameter_validation.get(endpoint).get(k)
            if not _is_validate_func:
                raise InvalidParameter(
                    '%s parameter is invalid' % k
                )
            if not _is_validate_func(v):
                raise InvalidParameter(
                    '%s parameter has invalid value %s' % (k, str(v))
                )

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _validate(parameter_validation, endpoint, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def make_url(*args):
    return ''.join(args)
