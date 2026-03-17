from sqlalchemy.orm import Session
from models import Producto 
import dtos

def get_productos(db: Session):
    return db.query(Producto).all()

def find_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def crear_producto(db: Session, producto: dtos.Producto_Create):
    db_producto = Producto(nombre=producto.nombre, precio=producto.precio)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def actualizar_producto(db: Session, producto_id:int, producto_update: dtos.Producto_Create):
    db_producto = find_producto(db, producto_id)
    if db_producto:
        db_producto.nombre = producto_update.nombre
        db_producto.precio = producto_update.precio
        db.commit()  
        db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    db_producto = find_producto(db, producto_id)
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto