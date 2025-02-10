from pydantic import BaseModel
from typing import Optional

class OrderOut(BaseModel):
    id: int
    usuario_id: int
    quantidade: int
    preco_total: float
    endereco_entrega: str
    status: str

    class Config:
        orm_mode = True


class OrderIn(BaseModel):
    usuario_id: int
    quantidade: int
    preco_total: float
    endereco_entrega: str
    status: str

    class Config:
        orm_mode = True