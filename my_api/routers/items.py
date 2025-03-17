from fastapi import APIRouter, Depends, HTTPException
from typing import List
import mysql.connector
from ..database import get_db # Verifica esta línea
from ..models import Item

router = APIRouter()

@router.get("/items/", response_model=List[Item])
def read_items(db: mysql.connector.MySQLConnection = Depends(get_db)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return items

@router.post("/items/", response_model=Item)
def create_item(item: Item, db: mysql.connector.MySQLConnection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("INSERT INTO items (name, description, price) VALUES (%s, %s, %s)",
                   (item.name, item.description, item.price))
    db.commit()
    return item

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: mysql.connector.MySQLConnection = Depends(get_db)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, db: mysql.connector.MySQLConnection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("UPDATE items SET name = %s, description = %s, price = %s WHERE id = %s",
                   (item.name, item.description, item.price, item_id))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int, db: mysql.connector.MySQLConnection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}