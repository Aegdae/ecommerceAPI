from sqlalchemy.future import select
from models.user import User
from database.databaseUser import get_db
from passlib.context import CryptContext

myctx = CryptContext(schemes=["Bcrypt"], default="Bcrypt")

class UserRepository:
    def __init__(self, db):
        self.db = db

    
    async def verify_email(self, email: str):
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
    
    
    def hashed_password(self, senha: str):
        hashed_password = myctx.hash(senha)
        return hashed_password
    