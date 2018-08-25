import subprocess
import os.path
import json
import dateutil.parser
import time

from database import Business, Review

for business in Business.where('checked', None).get():
    if (business.id > 0) and (business.reviews.count() == 0):
        time.sleep(5)

        print(f'{business.id}: {business.name}, {2797 - business.id} left')

        data = subprocess.check_output(['./bin/reviews', business.remote_id])
        parsed = json.loads(data.decode('utf-8'))

        reviews = parsed.get('reviews')

        if reviews is not None:
            for r in reviews:
                d = dateutil.parser.parse(r['date'])
                review = Review.create(
                    business_id=business.id,
                    content=r['content'],
                    date=round(d.timestamp()),
                    rating=r['rating']
                )

            business.update({'checked': round(time.time())})
        else:
            error = parsed.get('error')
            raise RuntimeError(error)


