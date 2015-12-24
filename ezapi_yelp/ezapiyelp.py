from requests_oauthlib import OAuth1Session


class EZapiYelp:

    # Simple error that prints predefined message
    class EZerror(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    # requires consumer_key, consumer_secret, access_token, access_token_secret
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.session = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

        # search api type constraints
        self.search_setting = {
            'term': str,
            'limit': int,
            'offset': int,
            'sort': int,
            'category_filter': str,
            'radius_filter': int,
            'deals_filter': bool,
            'actionlinks': bool,
            'location': str,
            'cll': str,
            'bounds': str,
            'll': str,
        }

        # business api type constraints
        self.business_setting = {
            'cc': str,
            'lang': bool,
            'lang_filter': bool,
            'actionlinks': bool,
        }

        # phone_search api type constraints
        self.phone_search_setting = {
            'cc': str,
            'lang': bool,
            'lang_filter': bool,
            'phone': str,
        }

        # Yelp V2 api
        self.apiv2 = 'https://api.yelp.com/v2/'

    # check the correctness of parameter type, raise error if type mismatched
    def params_check(self, setting, **kwargs):
        for k, v in kwargs.iteritems():
            if k not in setting:
                mssg = 'Yelp V2 api| does noe have parameter: ' + k
                raise EZapiYelp.EZerror(mssg)
            elif not isinstance(v, setting[k]):
                mssg = "Yelp V2 api| parameter: " + k + ' should be ' + str(setting[k])
                raise EZapiYelp.EZerror(mssg)
            else:
                pass

    def get_search_params(self, **kwargs):
        if 'bounds' in kwargs:
            try:
                items = kwargs['bounds'].split('|')
                [sw_lat, sw_long] = items[0].split(',')
                [ne_lat, ne_long] = items[1].split(',')
                sw_lat = float(sw_lat)
                sw_long = float(sw_long)
                ne_lat = float(ne_lat)
                ne_long = float(ne_long)
            except:
                mssg = 'Yelp V2 api| parameter: bounds should be "sw_lat,sw_long|ne_lat, ne_long"'
        if 'll' in kwargs:
            values = kwargs['ll'].split(',')
            if len(values) < 2 or len(values) > 5:
                mssg = 'Yelp V2 api| parameter: ll should at least contain a set of 2 items'
                raise EZapiYelp.EZerror(mssg)
            else:
                try:
                    for v in values:
                        v = float(v)
                except:
                    mssg = 'Yelp V2 api| parameter: ll should be double'
                    raise EZapiYelp.EZerror(mssg)        
        if 'location' not in kwargs and 'bounds' not in kwargs and 'll' not in kwargs:
            mssg = 'Yelp V2 api| required parameter: location/bounds/ll'
            raise EZapiYelp.EZerror(mssg)

        if 'cll' in kwargs:
            values = kwargs['cll'].split(',')
            if len(values)!= 2:
                mssg = 'Yelp V2 api| parameter: cll should contain a set of 2 items'
                raise EZapiYelp.EZerror(mssg)
            else:
                try:
                    latitude, longitude = float(values[0]), float(values[1])
                except:
                    mssg = 'Yelp V2 api| parameter: cll type should be double'
                    raise EZapiYelp.EZerror(mssg)

        self.params_check(self.search_setting, **kwargs)
        return kwargs

    def get_business_params(self, **kwargs):
        self.params_check(self.business_setting, **kwargs)
        return kwargs

    def get_phone_search_params(self, **kwargs):
        if 'phone' not in kwargs:
            mssg = 'Yelp V2 api| required parameter: phone'
            raise EZapiYelp.EZerror(mssg)
        self.params_check(self.phone_search_setting, **kwargs)
        return kwargs

    # sample Request, GET https://api.yelp.com/v2/search?param1=v1&param2=v2
    def search(self, **kwargs):
        params = self.get_search_params(**kwargs)
        res = self.session.get(self.apiv2+'search', params = params)
        res = res.json()
        if 'error' not in res:
            return res
        else:
            raise EZapiYelp.EZerror(res['error']['text'])

    # sample Request, GET https://api.yelp.com/v2/business/{{id}}?param1=v1&param2=v2
    def business(self, id, **kwargs):
        if not isinstance(id, str):
            mssg = 'Yelp V2 api| parameter: id should be ' + str(str)
            raise EZapiYelp.EZerror(mssg)
        params = self.get_business_params(**kwargs)
        res = self.session.get(self.apiv2+'business/'+id, params = params)
        res = res.json()
        if 'error' not in res:
            return res
        else:
            raise EZapiYelp.EZerror(res['error']['text'])

    # sample Request, GET https://api.yelp.com/v2/phone_search?param1=v1&param2=v2
    def phone_search(self, **kwargs):
        params = self.get_phone_search_params(**kwargs)
        res = self.session.get(self.apiv2+'phone_search', params = params)
        res = res.json()
        if 'error' not in res:
            return res
        else:
            raise EZapiYelp.EZerror(res['error']['text'])

