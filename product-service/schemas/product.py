from pydantic import BaseModel
from typing import Optional


class ProductOut(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade_estoque: float
    categoria: str

    class Config:
        orm_mode = True 



class ProductIn(BaseModel):
    nome: str
    descricao: str
    preco: float
    quantidade_estoque: float
    categoria: str

    class Config:
        orm_mode = True