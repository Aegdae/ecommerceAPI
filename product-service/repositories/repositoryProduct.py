from sqlalchemy.future import select
from models.product import Product
from database.databaseProduct import get_db

class ProductRepository:
    def __init__(self, db):
        self.db = db