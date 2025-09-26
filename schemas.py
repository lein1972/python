# app/schemas.py 
from pydantic import BaseModel 
 
class ClienteBase(BaseModel): 
    nombre: str 
    apellido: str 
    email: str 
 
class ClienteCreate(ClienteBase): 
    pass 
 
class Cliente(ClienteBase): 
    id: int 
 
    class Config: 
        from_attributes = True