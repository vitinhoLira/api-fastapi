from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import auth
from app.database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post("/register", response_model=schemas.UsuarioResponse)
def registrar(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    existe = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    hash_senha = auth.gerar_hash(usuario.senha)
    novo_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=hash_senha,
        role="usuario"  # ← aqui você define a role padrão
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@router.post("/login", response_model=schemas.TokenOut)
def login(dados: schemas.LoginInput, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == dados.email).first()
    if not usuario or not auth.verificar_senha(dados.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = auth.criar_token({"sub": str(usuario.id)})
    return {"access_token": token, "token_type": "bearer"}
