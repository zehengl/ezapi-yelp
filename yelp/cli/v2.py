import click
import json

from yelp.api.v2 import Yelp


@click.group()
@click.option('--consumer_key', envvar='consumer_key')
@click.option('--consumer_secret', envvar='consumer_secret')
@click.option('--token', envvar='token')
@click.option('--token_secret', envvar='token_secret')
@click.pass_context
def yelp2(ctx, consumer_key=None, consumer_secret=None, token=None, token_secret=None):
    assert consumer_key and consumer_secret and token and token_secret, \
        """
        Please specify credentials for yelp api v2:
        Either set as env variable:
            export consumer_key = xxxx
            export consumer_secret = xxxx
            export token = xxxx
            export token_secret = xxxx
            yelp2 ...
        Or pass in as options:
            yelp2 --consumer_key='xxxx' --consumer_secret='xxxx' --token='xxxx' --token_secret='xxxx' ...
        """

    yelp = Yelp(
        consumer_key,
        consumer_secret,
        token,
        token_secret,
    )
    ctx.obj['yelp'] = yelp


@yelp2.command()
@click.option('--term', type=str)
@click.option('--limit', type=int)
@click.option('--offset', type=int)
@click.option('--sort', type=int)
@click.option('--category_filter', type=str)
@click.option('--radius_filter', type=str)
@click.option('--deals_filter', type=bool)
@click.option('--location', type=str)
@click.option('--cll', type=str)
@click.option('--bounds', type=str)
@click.option('--ll', type=str)
@click.option('--cc', type=str)
@click.option('--lang', type=str)
@click.option('--actionlinks', type=bool)
@click.option('--indent', default=None, type=int)
@click.pass_context
def search(ctx,
           term, limit, offset, sort, category_filter, radius_filter, deals_filter,
           location, cll, bounds, ll,
           cc, lang,
           actionlinks,
           indent,
           ):
    parameters = {}
    if term:
        parameters['term'] = str(term)
    if limit:
        parameters['limit'] = limit
    if offset:
        parameters['offset'] = offset
    if sort:
        parameters['sort'] = sort
    if category_filter:
        parameters['category_filter'] = str(category_filter)
    if radius_filter:
        parameters['radius_filter'] = str(radius_filter)
    if deals_filter:
        parameters['deals_filter'] = str(deals_filter)
    if location:
        parameters['location'] = str(location)
    if cll:
        parameters['cll'] = str(cll)
    if bounds:
        parameters['bounds'] = str(bounds)
    if ll:
        parameters['ll'] = str(ll)
    if cc:
        parameters['cc'] = str(cc)
    if lang:
        parameters['lang'] = str(lang)
    if actionlinks:
        parameters['actionlinks'] = actionlinks
    print json.dumps(ctx.obj['yelp'].search(**parameters), indent=indent)


@yelp2.command()
@click.argument('business_id', nargs=1)
@click.option('--cc', type=str)
@click.option('--lang', type=str)
@click.option('--actionlinks', type=bool)
@click.option('--indent', default=None, type=int)
@click.pass_context
def business(ctx,
             business_id,
             cc, lang, actionlinks,
             indent,
             ):
    parameters = {}
    if cc:
        parameters['cc'] = str(cc)
    if lang:
        parameters['lang'] = str(lang)
    if actionlinks:
        parameters['actionlinks'] = actionlinks
    print json.dumps(ctx.obj['yelp'].business(business_id, **parameters), indent=indent)


@yelp2.command()
@click.option('--phone', type=str)
@click.option('--cc', type=str)
@click.option('--category', type=str)
@click.option('--indent', default=None, type=int)
@click.pass_context
def phone_search(ctx,
                 phone, cc, category,
                 indent,
                 ):
    parameters = {}
    if phone:
        parameters['phone'] = str(phone)
    if cc:
        parameters['cc'] = str(cc)
    if category:
        parameters['category'] = str(category)
    print json.dumps(ctx.obj['yelp'].phone_search(**parameters), indent=indent)


def run():
    yelp2(obj=dict())
