import geojson
from shapely.geometry import shape, Point
from database import Business
import json

def feature_shape(feature):
    return shape(feature['geometry'])

def neighborhood_shapes(neighborhood_name):
    features = filter(
        lambda f: f['properties']['@id'].split('/')[-1] == neighborhood_name,
        geo.features
    )
    return map(feature_shape, features)

def businesses_in_shape(s):
    return list(
        filter(
            lambda b: s.contains(Point(b.longitude, b.latitude)),
            list(Business.all())
        )
    )

def businesses_in_neighborhood(neighborhood):
    return [ b for s in neighborhood_shapes(neighborhood) for b in businesses_in_shape(s) ]

def review_count(neighborhood):
    return sum(
        map(
            lambda b: b.reviews.count(),
            businesses_in_neighborhood(neighborhood)
        )
    )

def initial_neighborhood_data(neighborhood):
    return {
        'business_ids': list(map(lambda b: b.id, businesses_in_neighborhood(neighborhood))),
        'review_count': review_count(neighborhood),
        'word_data': {}
    }

def create_initial_results_file():
    data = open('geo/pediacitiesnycneighborhoods.geojson').read()
    geo = geojson.loads(data)
    ids = set(map(lambda f: f['properties']['@id'].split('/')[-1], geo.features))
    results = { n: initial_neighborhood_data(n) for n in ids }
    with open('results/new_york.json', 'w') as outfile:
        json.dump(results, outfile)

# create_initial_results_file()
