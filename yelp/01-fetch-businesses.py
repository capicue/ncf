import requests
import os
from dotenv import load_dotenv
from yarl import URL
import csv

DATA_SET = 'sfRestaurants'

load_dotenv('.env')

API_KEY = os.environ['API_KEY']

PARAMS = {
    'nyCoffee': {
        'origin': (40.72, -74.02),
        'padding': 60,
        'categories': 'coffee'
    },
    'sfCoffee': {
        'origin': (37.75, -122.45),
        'padding': 20,
        'categories': 'coffee'
    },
    'toledoRestaurants': {
        'origin': (41.65,-83.54),
        'padding': 20,
        'categories': 'restaurants'
    },
    'sfRestaurants': {
        'origin': (37.75, -122.45),
        'padding': 20,
        'categories': 'restaurants'
    }
}

ORIGIN = PARAMS[DATA_SET]['origin']
PADDING = PARAMS[DATA_SET]['padding']
CATEGORIES = PARAMS[DATA_SET]['categories']

def radius(n):
    for i in range(-n, n):
        yield (i, n)
    for i in range(-n, n):
        yield (n, -i)
    for i in range(-n, n):
        yield (-i, -n)
    for i in range(-n, n):
        yield (-n, i)

def traverse(n):
    yield (0, 0)
    for r in range(1, n+1):
        for offset in radius(r):
            yield offset

def search_url(params):
    return URL.build(
        scheme='https',
        host='api.yelp.com',
        path='v3/businesses/search',
        query=params
    )

def business_info(business):
    return {
        'id': business['id'],
        'name': business['name'],
        'review_count': business['review_count'],
        'categories': ';'.join(map(lambda c: c['alias'], business['categories'])),
        'rating': business['rating'],
        'latitude': business['coordinates']['latitude'],
        'longitude': business['coordinates']['longitude'],
        'location': ', '.join(business['location']['display_address']),
        'price': business.get('price'),
        'phone': business['phone']
    }

def get_all(location, page=0):
    limit = 50

    response = requests.get(
        search_url({
            'latitude':str(location[0]),
            'longitude':str(location[1]),
            'radius':'500',
            'limit':str(limit),
            'categories':CATEGORIES
        }),
        headers={'Authorization': f'Bearer {API_KEY}'}
    ).json()

    assert response['total'] < 1000, f'Too many results for ({location[0]}, {location[1]})'

    businesses = list(map(business_info, response['businesses']))

    lastPage = (page + 1) * limit >= response['total']

    if lastPage:
        return businesses
    else:
        return businesses + get_all(location, page+1)

with open(f'data/{DATA_SET}.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'review_count', 'categories', 'rating',
            'latitude', 'longitude', 'location', 'price', 'phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for offset in traverse(PADDING):
        print(offset)

        location = (
            round(ORIGIN[0] + (offset[0]/200), 3),
            round(ORIGIN[1] + (offset[1]/200), 3)
        )

        for business in get_all(location):
            writer.writerow(business)
