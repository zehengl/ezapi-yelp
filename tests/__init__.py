from ConfigParser import SafeConfigParser
from os import path


config_path = path.abspath(path.dirname(__file__))
config_file = '%s/credentials.conf' % config_path

assert path.isfile(config_file), \
    """
    Please use your credentials for testing
    1. touch tests/credentials.conf
    2. add your credentials in the config file
        [v2]
        consumer_key = xxxx
        consumer_secret = xxxx
        token = xxxx
        token_secret = xxxx

        [v3]
        app_id = xxxx
        app_secret = xxxx
    """

config = SafeConfigParser()
config.read(config_file)

assert config.get('v2', 'consumer_key'), 'missing v2 consumer_key'
assert config.get('v2', 'consumer_secret'), 'missing v2 consumer_secret'
assert config.get('v2', 'token'), 'missing v2 token'
assert config.get('v2', 'token_secret'), 'missing v2 token_secret'

assert config.get('v3', 'app_id'), 'missing v3 app_id'
assert config.get('v3', 'app_secret'), 'missing v3 app_secret'

credential_v2 = {
    'consumer_key': config.get('v2', 'consumer_key'),
    'consumer_secret': config.get('v2', 'consumer_secret'),
    'token': config.get('v2', 'token'),
    'token_secret': config.get('v2', 'token_secret'),
}

credential_v3 = {
    'app_id': config.get('v3', 'app_id'),
    'app_secret': config.get('v3', 'app_secret'),
}


def is_error(response):
    """
    Utility function to check if a response is error
    :param response: dict
    :return: boolean
    """
    return response.get('error') is not None
