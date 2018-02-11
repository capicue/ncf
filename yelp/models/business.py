from orator import Model
from orator.orm import belongs_to_many
from orator.orm import has_many
import models.category
import models.review


class Business(Model):
    __timestamps__ = False
    __guarded__ = ['id']

    @belongs_to_many('categorizations')
    def categories(self):
        return models.category.Category

    @has_many
    def reviews(self):
        return models.review.Review
