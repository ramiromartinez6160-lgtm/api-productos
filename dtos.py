from pydantic import BaseModel

class Producto_Create(BaseModel):
    nombre: str
    precio: float

class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: float