# main.py 
from fastapi import FastAPI 
from app.routers import clientes 

app = FastAPI() 
app.include_router(clientes.router) 

@app.get("/") 
def read_root(): 
    return {"Hello": "World"}