from sqlalchemy.future import select
from models.order import Order
from database.databaseOrder import get_db

class OrderRepository:
    def __init__(self, db):
        self.db = db