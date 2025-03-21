# auth/auth_handler.py
import jwt
import datetime
from passlib.context import CryptContext
from fastapi import HTTPException, status

JWT_SECRET = "tu_secreto_super_seguro"
JWT_ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def encode_token(username):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        "iat": datetime.datetime.utcnow(),
        "sub": username,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

# auth/auth_handler.py
JWT_SECRET = "tu_secreto_super_seguro"
JWT_ALGORITHM = "HS256"

def decode_token(token):
    print(f"Token recibido para decodificar: {token}")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        print(f"Payload decodificado: {payload}")
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        print("Error: Token expirado")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
    except jwt.InvalidTokenError:
        print("Error: Token invalido")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalido")
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Error al decodificar token: {e}")