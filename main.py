from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Teléfono", "precio": 800},
    {"id": 3, "nombre": "Tablet", "precio": 500},
]

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

@app.get("/productos")
async def obtener_productos():
    return productos

@app.get("/productos/{producto_id}")
async def obtener_producto(producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto
    return {"error": "Producto no encontrado"}

@app.post("/productos")
async def crear_producto(producto: Producto):
    productos.append(producto.dict())
    return producto