from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    cpf = Column(String(14),unique=True ,nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, nome={self.nome}, email={self.email}, senha={self.senha}, cpf={self.cpf})>"