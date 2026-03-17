from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, dtos
import productos.crud as crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():  
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/productos/{producto_id}", response_model=dtos.ProductoResponse)
def get_producto(producto_id, db: Session = Depends(get_db)):
    db_producto = crud.find_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="No existe el producto")
    return db_producto

@app.get("/productos", response_model=list[dtos.ProductoResponse])
def get_productos(db: Session = Depends(get_db)):
    productos = crud.get_productos(db)
    return productos   

@app.post("/productos", response_model=dtos.ProductoResponse)
def crear_producto(producto: dtos.Producto_Create, db: Session = Depends(get_db)):
    return crud.crear_producto(db=db, producto=producto)

@app.put("/productos/{producto_id}", response_model=dtos.Producto_Create)
def actualizar_producto(producto_id: int, producto: dtos.Producto_Create, db: Session = Depends(get_db)):
    producto_db = crud.actualizar_producto(db=db, producto_id=producto_id, producto_update=producto)
    if producto_db is None:
        raise HTTPException(status_code=404, detail="No existe el producto")
    return producto_db

@app.delete("/productos/{producto_id}", response_model=dtos.ProductoResponse)
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)): 
    producto_db = crud.eliminar_producto(db=db, producto_id=producto_id)
    if producto_db is None:
        raise HTTPException(status_code=404, detail="No existe el producto")
    return producto_db