import requests
import os
from dotenv import load_dotenv
from yarl import URL
import csv

DATA_SET = 'nyCoffee'

load_dotenv('.env')

API_KEY = os.environ['API_KEY']

PARAMS = {
    'nyCoffee': {
        'origin': (40.72, -74.02),
        'padding': 30,
        'categories': 'coffee'
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

def searchUrl(params):
    return URL.build(
        scheme='https',
        host='api.yelp.com',
        path='v3/businesses/search',
        query=params
    )

def businessInfo(business):
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

def getAll(location, page=0):
    limit = 50

    response = requests.get(
        searchUrl({
            'latitude':str(location[0]),
            'longitude':str(location[1]),
            'radius':'1000',
            'limit':str(limit),
            'categories':CATEGORIES
        }),
        headers={'Authorization': f'Bearer {API_KEY}'}
    ).json()

    assert response['total'] < 1000, f'Too many results for ({location[0]}, {location[1]})'

    businesses = list(map(businessInfo, response['businesses']))

    lastPage = (page + 1) * limit >= response['total']

    if lastPage:
        return businesses
    else:
        return businesses + getAll(location, page+1)

with open(f'data/{DATA_SET}.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'review_count', 'categories', 'rating',
            'latitude', 'longitude', 'location', 'price', 'phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for offset in traverse(PADDING):
        print(offset)

        location = (
            round(ORIGIN[0] + (offset[0]/100), 2),
            round(ORIGIN[1] + (offset[1]/100), 2)
        )

        for business in getAll(location):
            writer.writerow(business)
