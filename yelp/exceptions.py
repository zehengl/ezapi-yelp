class YelpException(Exception):
    """Yelp Exception"""
    def __init__(self, *args, **kwargs):
        super(YelpException, self).__init__(*args, **kwargs)


class InvalidParameter(YelpException):
    """An invalid parameter occurred"""


class InvalidEndpoint(YelpException):
    """An invalid endpoint occurred"""


class InvalidTransactionType(YelpException):
    """An invalid transaction type occurred"""
