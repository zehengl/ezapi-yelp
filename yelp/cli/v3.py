import click
import json

from yelp.api.v3 import Yelp


@click.group()
@click.option('--app_id', envvar='app_id')
@click.option('--app_secret', envvar='app_secret')
@click.pass_context
def yelp_fusion(ctx, app_id=None, app_secret=None):
    assert app_id and app_secret, \
        """
        Please specify credentials for yelp api fusion/v3:
        Either set as env variable:
            export app_id = xxxx
            export app_secret = xxxx
            yelp-fusion ...
        Or pass in as options:
            fusion --app_id='xxxx' --app_secret='xxxx' ...
        """
    yelp = Yelp(
        app_id,
        app_secret,
    )
    ctx.obj['yelp'] = yelp


@yelp_fusion.command()
@click.option('--term', type=str)
@click.option('--location', type=str)
@click.option('--latitude', type=float)
@click.option('--longitude', type=float)
@click.option('--radius', type=int)
@click.option('--categories', type=str)
@click.option('--locale', type=str)
@click.option('--limit', type=int)
@click.option('--offset', type=int)
@click.option('--sort_by', type=str)
@click.option('--price', type=str)
@click.option('--open_now', type=bool)
@click.option('--open_at', type=int)
@click.option('--attributes', type=str)
@click.option('--indent', default=None, type=int)
@click.pass_context
def search(ctx,
           term, location, latitude, longitude, radius,
           categories, locale, limit, offset, sort_by,
           price, open_now, open_at, attributes,
           indent,
           ):
    parameters = {}
    if term:
        parameters['term'] = str(term)
    if location:
        parameters['location'] = str(location)
    if latitude:
        parameters['latitude'] = latitude
    if longitude:
        parameters['longitude'] = longitude
    if radius:
        parameters['radius'] = radius
    if categories:
        parameters['categories'] = str(categories)
    if locale:
        parameters['locale'] = str(locale)
    if limit:
        parameters['limit'] = limit
    if offset:
        parameters['offset'] = offset
    if sort_by:
        parameters['sort_by'] = str(sort_by)
    if price:
        parameters['price'] = str(price)
    if open_now:
        parameters['open_now'] = open_now
    if open_at:
        parameters['open_at'] = open_at
    if attributes:
        parameters['attributes'] = str(attributes)
    print json.dumps(ctx.obj['yelp'].search(**parameters), indent=indent)


@yelp_fusion.command()
@click.option('--phone', type=str)
@click.option('--indent', default=None, type=int)
@click.pass_context
def phone_search(ctx, phone, indent):
    parameters = {}
    if phone:
        parameters['phone'] = str(phone)
    print json.dumps(ctx.obj['yelp'].phone_search(**parameters), indent=indent)


@yelp_fusion.command()
@click.argument('transaction_type', nargs=1)
@click.option('--latitude', type=float)
@click.option('--longitude', type=float)
@click.option('--location', type=str)
@click.option('--indent', default=None, type=int)
@click.pass_context
def transaction_search(ctx,
                       transaction_type,
                       latitude, longitude, location,
                       indent,
                       ):
    parameters = {}
    if latitude:
        parameters['latitude'] = latitude
    if longitude:
        parameters['longitude'] = longitude
    if location:
        parameters['location'] = str(location)
    print json.dumps(ctx.obj['yelp'].transaction_search(transaction_type, **parameters), indent=indent)


@yelp_fusion.command()
@click.argument('business_id', nargs=1)
@click.option('--indent', default=None, type=int)
@click.pass_context
def business(ctx, business_id, indent):
    print json.dumps(ctx.obj['yelp'].business(business_id), indent=indent)


@yelp_fusion.command()
@click.argument('business_id', nargs=1)
@click.option('--locale', type=str)
@click.option('--indent', default=None, type=int)
@click.pass_context
def reviews(ctx, business_id, locale, indent):
    parameters = {}
    if locale:
        parameters['locale'] = str(locale)
    print json.dumps(ctx.obj['yelp'].reviews(business_id), indent=indent)


@yelp_fusion.command()
@click.option('--text', type=str)
@click.option('--latitude', type=float)
@click.option('--longitude', type=float)
@click.option('--locale', type=str)
@click.option('--indent', default=None, type=int)
@click.pass_context
def autocomplete(ctx,
                 text, latitude, longitude, locale,
                 indent,
                 ):
    parameters = {}
    if text:
        parameters['text'] = str(text)
    if latitude:
        parameters['latitude'] = latitude
    if longitude:
        parameters['longitude'] = longitude
    if locale:
        parameters['locale'] = str(locale)
    print json.dumps(ctx.obj['yelp'].autocomplete(**parameters), indent=indent)


def run():
    yelp_fusion(obj=dict())
