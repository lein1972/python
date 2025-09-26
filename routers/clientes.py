# app/routers/clientes.py 
from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from typing import List 
 
from .. import models, schemas, database 
 
router = APIRouter( 
    prefix="/clientes", 
    tags=["clientes"] 
) 
 
@router.post("/", response_model=schemas.Cliente, status_code=status.HTTP_201_CREATED) 
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(database.get_db)): 
    db_cliente = models.Cliente(**cliente.dict()) 
    db.add(db_cliente) 
    db.commit() 
    db.refresh(db_cliente) 
    return db_cliente 
 
@router.get("/", response_model=List[schemas.Cliente]) 
def listar_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)): 
    clientes = db.query(models.Cliente).offset(skip).limit(limit).all() 
    return clientes 
 
@router.get("/{cliente_id}", response_model=schemas.Cliente) 
def obtener_cliente(cliente_id: int, db: Session = Depends(database.get_db)): 
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first() 
    if cliente is None: 
        raise HTTPException(status_code=404, detail="Cliente no encontrado") 
    return cliente