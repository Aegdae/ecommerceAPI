from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Product(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    preco = Column(Numeric, nullable=False)
    quantidade_estoque = Column(Numeric, nullable=False)
    categoria = Column(String(255), nullable=False)


    def __repr__(self):
        return f"<Product(id={self.id}, nome={self.nome}, descicao={self.descricao}, preco={self.preco}, quantidade_estoque={self.quantidade_estoque}, categoria={self.categoria})>"