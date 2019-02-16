import requests
import wrapt

ENDPOINT = "https://api.yelp.com/v3"


def any_required_kwargs(*required_kwargs_list):
    """
    Decorator to check if criteria of required kwargs are met

    Raises:
        RuntimeError: a bad client request

    Returns:
        func: decorated function
    """

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        compliances = [
            all([kwarg in kwargs for kwarg in required_kwargs])
            for required_kwargs in required_kwargs_list
        ]

        if any(compliances):
            return wrapped(*args, **kwargs)

        compliant_sets = [
            f'({" and ".join(required_kwargs)})'
            for required_kwargs in required_kwargs_list
        ]
        msg = f"required kwargs: {' or '.join(compliant_sets)}"

        raise RuntimeError(f"{msg}")

    return wrapper


@wrapt.decorator
def process_response(wrapped, instance, args, kwargs):
    """
    Decorator to process requests.Response

    Raises:
        Exception: Service Unavailable

    Returns:
        dict: json data
    """

    try:
        resp = wrapped(*args, **kwargs)

    except (requests.ConnectionError, requests.Timeout) as e:
        raise Exception("Service Unavailable") from e

    else:
        resp.raise_for_status()
        return resp.json()


class YelpFusion:
    def __init__(self, token):
        """
        Constructor

        Args:
            token (str): the API Key, see https://www.yelp.com/developers/v3/manage_app
        """

        self.session = requests.Session()
        self.session.headers.update({"authorization": f"Bearer {token}"})

    @any_required_kwargs(["location"], ["latitude", "longitude"])
    @process_response
    def business_search(self, **kwargs):
        """
        GET /businesses/search

        Returns:
            dict: This endpoint returns up to 1000 businesses based on the provided search criteria.
        """

        return self.session.get(f"{ENDPOINT}/businesses/search", params=kwargs)

    @any_required_kwargs(["phone"])
    @process_response
    def phone_search(self, **kwargs):
        """
        GET /businesses/search/phone

        Returns:
            dict: This endpoint returns a list of businesses based on the provided phone number.
        """

        return self.session.get(f"{ENDPOINT}/businesses/search/phone", params=kwargs)

    @any_required_kwargs(["location"], ["latitude", "longitude"])
    @process_response
    def transaction_search(self, transaction_type, **kwargs):
        """
        GET /transactions/{transaction_type}/search

        Args:
            transaction_type (str): a transaction type

        Returns:
            dict: This endpoint returns a list of businesses which support food delivery transactions.
        """

        return self.session.get(
            f"{ENDPOINT}/transactions/{transaction_type}/search", params=kwargs
        )

    @process_response
    def business_details(self, business_id, **kwargs):
        """
        GET /businesses/{id}

        Args:
            business_id (str): a business ID

        Returns:
            dict: This endpoint returns detailed business content.
        """

        return self.session.get(f"{ENDPOINT}/businesses/{business_id}", params=kwargs)

    @any_required_kwargs(["name", "address1", "city", "state", "country"])
    @process_response
    def business_match(self, **kwargs):
        """
        GET /businesses/matches

        Returns:
            dict: This endpoint lets you match business data from other sources against businesses on Yelp,
            based on provided business information.
        """

        return self.session.get(f"{ENDPOINT}/businesses/matches", params=kwargs)

    @process_response
    def reviews(self, business_id, **kwargs):
        """
        GET /businesses/{id}/reviews

        Args:
            business_id ([type]): a business ID

        Returns:
            dict: This endpoint returns up to three review excerpts for a given business
            ordered by Yelp's default sort order.
        """

        return self.session.get(
            f"{ENDPOINT}/businesses/{business_id}/reviews", params=kwargs
        )

    @any_required_kwargs(["text"])
    @process_response
    def autocomplete(self, **kwargs):
        """
        GET /autocomplete

        Returns:
            dict: This endpoint returns autocomplete suggestions for
            search keywords, businesses and categories, based on the input text.
        """

        return self.session.get(f"{ENDPOINT}/autocomplete", params=kwargs)

    @process_response
    def event_lookup(self, event_id, **kwargs):
        """
        GET /events/{id}

        Args:
            event_id (str): an event ID

        Returns:
            dict: This endpoint returns the detailed information of a Yelp event.
        """

        return self.session.get(f"{ENDPOINT}/events/{event_id}", params=kwargs)

    @process_response
    def event_search(self, **kwargs):
        """
        GET /events

        Returns:
            dict: This endpoint returns events based on the provided search criteria.
        """

        return self.session.get(f"{ENDPOINT}/events", params=kwargs)

    @any_required_kwargs(["location"], ["latitude", "longitude"])
    @process_response
    def featured_event(self, **kwargs):
        """
        GET /events/featured

        Returns:
            dict: This endpoint returns the featured event for a given location.
        """

        return self.session.get(f"{ENDPOINT}/events/featured", params=kwargs)

    @process_response
    def all_categories(self, **kwargs):
        """
        GET /categories

        Returns:
            dict: This endpoint returns all Yelp business categories across all locales by default.
        """

        return self.session.get(f"{ENDPOINT}/categories", params=kwargs)

    @process_response
    def category_details(self, alias, **kwargs):
        """
        GET /categories/{alias}

        Args:
            alias (str): a Yelp category alias

        Returns:
            dict: This endpoint returns detailes about the Yelp category specified by a Yelp category alias.
        """

        return self.session.get(f"{ENDPOINT}/categories/{alias}", params=kwargs)
