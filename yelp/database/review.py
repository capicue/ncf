from orator import Model
from orator.orm import belongs_to

import database.business


class Review(Model):
    __timestamps__ = False
    __guarded__ = ['id']

    @belongs_to
    def business(self):
        return database.business.Business
