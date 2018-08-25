from orator import Model
from orator.orm import belongs_to_many
from orator.orm import has_many

import database.category
import database.review

class Business(Model):
    __timestamps__ = False
    __guarded__ = ['id']

    @belongs_to_many('categorizations')
    def categories(self):
        return database.category.Category

    @has_many
    def reviews(self):
        return database.review.Review
