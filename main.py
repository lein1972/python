# main.py
from fastapi import FastAPI, Depends, HTTPException, status, Header
from auth import auth_routes, auth_handler

app = FastAPI()

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token no proporcionado")
    try:
        token = authorization.split(" ")[1]
        return auth_handler.decode_token(token)
    except IndexError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Formato de token incorrecto")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Error al decodificar token: {e}")

@app.get("/protected")
def protected_route(username: str = Depends(get_current_user)):
    return {"username": username}

@app.get("/")
def read_root():
    return {"Hello": "World"}