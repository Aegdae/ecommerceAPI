from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Order(Base):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_total = Column(Numeric, nullable=False)
    endereco_entrega = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Order(id={self.id}, usuario_id={self.usuario_id}, quantidade={self.quantidade}, preco_total={self.preco_total}, endereco_entrega={self.endereco_entrega}, status={self.status})>"