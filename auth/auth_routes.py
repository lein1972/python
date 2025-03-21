# auth/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .auth_handler import get_password_hash, verify_password, encode_token
from database.database import add_user, get_user
from models.user_model import User

router = APIRouter()

@router.post("/register")
def register(user: User):
    if get_user(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario ya registrado")
    hashed_password = get_password_hash(user.password)
    add_user({"username": user.username, "password": hashed_password})
    return {"message": "Usuario creado"}

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    access_token = encode_token(user["username"])
    return {"access_token": access_token, "token_type": "bearer"}