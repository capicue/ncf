from orator import DatabaseManager, Model
import csv

from database import Business, Category

DATA_SET = 'sfRestaurants'

with open(f'data/{DATA_SET}.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for b in reader:
        business = Business.first_or_new(remote_id=b['id'])

        business.name         = b['name']
        business.review_count = b['review_count']
        business.rating       = b['rating']
        business.latitude     = b['latitude']
        business.longitude    = b['longitude']
        business.location     = b['location']
        business.price        = b['price']
        business.phone        = b['phone']

        business.save()

        for c in b['categories'].split(';'):
            category = Category.first_or_create(name=c)
            business.categories().save(category)
