import geojson
from shapely.geometry import mapping, shape, Point
from database import Business, Review, Category
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


#  rm -f test*; geoproject 'd3.geoTransverseMercator().rotate([74 + 30 / 60, -38 - 50 / 60]).fitSize([960, 960], d)' < pediacitiesnycneighborhoods.geojson > test.json; geo2svg -w 960 -h 960 < test.json > test.svg

data = open('geo/pediacitiesnycneighborhoods.geojson').read()
geo = geojson.loads(data)
ids = set(map(lambda f: f['properties']['@id'].split('/')[-1], geo.features))

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

def word_frequency_in_neighborhood(word, neighborhood_name):
    positives = 0
    total = 0

    for s in neighborhood_shapes(neighborhood_name):
        for b in businesses_in_shape(s):
            for r in b.reviews:
                total += 1
                if word in word_tokenize(r.content):
                    positives += 1
    return (positives, total)

def word_frequency(word):
    results = {}
    for neighborhood_name in ids:
        print(neighborhood_name)
        results[neighborhood_name] = word_frequency_in_neighborhood(word, neighborhood_name)
    return results


def get_percent(point):
    if point[1] > 0:
        return point[0] / point[1]
    else:
        return 0


for key, value in sorted(percents.items(), key=lambda p: (p[1],p[0])):
    print(f"{key}: {value}")






fdist = FreqDist(word.lower() for word in word_tokenize(r))
fdist
text = b.reviews.lists('content').join()
text = join(b.reviews.lists('content'))
text = b.reviews.lists('content').concat()
text = " ".join(b.reviews.lists('content'))
text
fdist = FreqDist(word.lower() for word in word_tokenize(text))
fdist
fdist
dir(fdist)
fdist.most_common
fdist.most_common[10]
fdist.most_common()
/a/
import re
re.split('[\s]')
re.split('[\s]', text)
re.split('[\s/]', text)
re.split('[\s/,]', text)
re.split('[\s/,\.]', text)
re.split('\W', text)
re.split('\W+', text)
word_tokenize(text)
re.sub('\W', '', text)
re.sub('[^\w ]', '', text)
re.sub('[^\w ']', '', text)
re.sub('[^\w \']', '', text)
nltk.bigrams(text)
big = nltk.bigrams(text)
next(big)
nltk.word_tokenize(text)
text.similar
fdist
fdist['delicious']
dir(fdist)
fdist.max
fdist.values
fdist.values()
fdist.values().sum()
sum(fdist.values())
fdist['delicious'] / sum(fdist.values())
fdist['disgusting'] / sum(fdist.values())
fdist['disgusting']
fdist['vegetarian']
fdist['old-timey']
fdist['healthy']
fdist['expensive']
print text
print(text)
fdist.freq('delicious')
fdist.freq('delicnotehu')
fdist.N()
fdist ?
fdist?
fdist.freq('Delicious')
fdist
fdist.freq('rainy')
Business.where_raw('')
Business.where_raw('latitude <= 40.75')
Business.where_raw('latitude <= 40.75').count()
Business.where_raw('latitude <= 40.75 and latitude > 40.749')
Business.where_raw('latitude <= 40.75 and latitude > 40.749').count
Business.where_raw('latitude <= 40.75 and latitude > 40.749').count()
lat = 40.71
lon = -74.01
Business.where_raw('latitude', '>=', lat).where('latitude', '<', lat + 0.001)
Business.where_raw('latitude', '>=', lat).where('latitude', '<', lat + 0.001).count()
    Business.where('latitude', '>=', lat).where('latitude', '<', lat + 0.001)
    Business.where('latitude', '>=', lat).where('latitude', '<', lat + 0.001).count()
def businessesAt(lat, lon):
    Business.where('latitude', '>=', lat).where('latitude', '<', lat + 0.001).where('longitude', '>=', lon).where('longitude', '<', lon + 0.001)
businessesAt(lat, lon)
businessesAt(lat, lon).count()
b = businessesAt(lat, lon)
b
def businessesAt(lat, lon):
    return Business.where('latitude', '>=', lat).where('latitude', '<', lat + 0.001).where('longitude', '>=', lon).where('longitude', '<', lon + 0.001)
businessesAt(lat, lon).count()
businessesAt(lat, lon).reviews()
dir(businessesAt(lat, lon))
def businessesAt(lat, lon):
    return Business.where_between('latitude', [lat, lat + 0.001]).where_between('longitude', [lon, lon + 001])
def businessesAt(lat, lon):
    return Business.where_between('latitude', [lat, lat + 0.001]).where_between('longitude', [lon, lon + 001])
def businessesAt(lat, lon):
    return Business.where_between('latitude', [lat, lat + 0.001]).where_between('longitude', [lon, lon + 0.001])
businessesAt(lat, lon)
businessesAt(lat, lon).count()
Review
from models.review import Review
db
dbdb.table('reviews') \
    .join('businesses', 'business_id', '=', 'reviews.business_id') \
    .where_between('business.latitude', [lat, lat + 0.001]) \
    .where_between('business.longitude', [lon, lon + 0.001])
db.table('reviews') \
    .join('businesses', 'business_id', '=', 'reviews.business_id') \
    .where_between('business.latitude', [lat, lat + 0.001]) \
    .where_between('business.longitude', [lon, lon + 0.001])
a = db.table('reviews') \
    .join('businesses', 'business_id', '=', 'reviews.business_id') \
    .where_between('business.latitude', [lat, lat + 0.001]) \
    .where_between('business.longitude', [lon, lon + 0.001])
a
a.count()
a = db.table('reviews') \
    .join('businesses', 'business_id', '=', 'reviews.business_id') \
    .where_between('businesses.latitude', [lat, lat + 0.001]) \
    .where_between('businesses.longitude', [lon, lon + 0.001])
a.count()
def reviewsAt(lat, lon):
    return db.table('reviews') \
        .join('businesses', 'business_id', '=', 'reviews.business_id') \
        .where_between('businesses.latitude', [lat, lat + 0.001]) \
        .where_between('businesses.longitude', [lon, lon + 0.001])
reviewsAt(lat, lon).count
reviewsAt(lat, lon).count()
reviewsAt(lat, lon).list('content')
reviewsAt(lat, lon).lists('content')
reviewsAt(lat, lon).lists('content').get()
reviewsAt(lat, lon).get()
reviewsAt(lat, lon).get().lists('content')
def reviewsAt(lat, lon):
    return db.table('reviews') \
        .join('businesses', 'business_id', '=', 'reviews.business_id') \
        .where_between('businesses.latitude', [lat, lat + 0.01]) \
        .where_between('businesses.longitude', [lon, lon + 0.01])
reviewsAt(lat, lon).get().lists('content')
reviewsAt(lat, lon).lists('content')
list(reviewsAt(lat, lon).lists('content'))
reviewsAt(lat, lon).count()
' '.join(reviewsAt(lat, lon).lists('content'))






POSITIVE
--------
- I'll be using this as my new study space in the future.
- Great place to study/grab a coffee/sit down and chat.
- It's still a really really great study spot!
- Definitely adding this to my rotating list of study spots!
- Free wifi, good coffee, good study space, good vibes.

NEGATIVE
--------
- It's not the best for studying or hanging out for too long.
- I don't know how anyone can say this place is conducive to working or
  studying.
- Definitely not a place to study, work, or relax.

MIXED/???
---------
- When first walking in, I thought this location would be my perfect new study
  spots.
- Lucky for me that music doesn't affect my studying!
- It's right across from Simple Studios so it makes a great spot to study lines
  before an audition.
- Staff was the nicest and they don't mind if you study.
- I went specifically to study and needed internet access.
- Part of why I love this place so much is because it reminds me of my study
  abroad days back in HK.
