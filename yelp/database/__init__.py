from orator import DatabaseManager, Model

from .business import Business
from .category import Category
from .review import Review

config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'database/yelp.db'
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)
