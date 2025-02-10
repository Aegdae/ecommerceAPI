from pydantic import BaseModel
from typing import Optional

class ProductOut(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    cpf: str

    class Cofing:
        orm_mode = True


class ProductIn(BaseModel):
    nome: str
    email: str
    senha: str
    cpf: str

    class Config:
        orm_mode = True