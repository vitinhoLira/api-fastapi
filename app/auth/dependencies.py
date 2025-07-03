# app/auth/dependencies.py
from fastapi import Depends, HTTPException, status
from app.models import Usuario
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuarios/login")

def get_usuario_logado(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credenciais_invalidas = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credenciais_invalidas
    except JWTError:
        raise credenciais_invalidas

    usuario = db.query(models.Usuario).filter(models.Usuario.id == int(user_id)).first()
    if usuario is None:
        raise credenciais_invalidas

    return usuario

def so_admins(usuario: Usuario = Depends(get_usuario_logado)):
    if usuario.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso permitido apenas para administradores"
        )
    return usuario
