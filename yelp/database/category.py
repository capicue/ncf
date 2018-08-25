from orator import Model
from orator.orm import belongs_to_many

import database.business


class Category(Model):
    __timestamps__ = False
    __guarded__ = ['id']

    @belongs_to_many('categorizations')
    def businesses(self):
        return database.business.Business
