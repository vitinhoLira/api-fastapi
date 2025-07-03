from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.auth.dependencies import get_usuario_logado, so_admins
from app.database import get_db

router = APIRouter(
    prefix="/perguntas",
    tags=["Perguntas"]
)

# 🔹 Criar uma nova pergunta
@router.post("/", response_model=schemas.PerguntaResponse)
def criar_pergunta(pergunta: schemas.PerguntaCreate, db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(so_admins)):
    # Verifica se o quizz existe
    quizz = db.query(models.Quizz).filter(models.Quizz.id == pergunta.quizz_id).first()
    if not quizz:
        raise HTTPException(status_code=404, detail="Quizz não encontrado")

    nova_pergunta = models.Pergunta(**pergunta.model_dump())
    db.add(nova_pergunta)
    db.commit()
    db.refresh(nova_pergunta)
    return nova_pergunta


# 🔹 Listar todas as perguntas
@router.get("/", response_model=list[schemas.PerguntaResponse])
def listar_perguntas(db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(get_usuario_logado)):
    return db.query(models.Pergunta).all()


# 🔹 Buscar uma pergunta por ID
@router.get("/{pergunta_id}", response_model=schemas.PerguntaResponse)
def buscar_pergunta(pergunta_id: int, db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(get_usuario_logado)):
    pergunta = db.query(models.Pergunta).filter(models.Pergunta.id == pergunta_id).first()
    if not pergunta:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada")
    return pergunta


# 🔹 Atualizar uma pergunta
@router.put("/{pergunta_id}", response_model=schemas.PerguntaResponse)
def atualizar_pergunta(pergunta_id: int, dados: schemas.PerguntaCreate, db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(so_admins)):
    pergunta = db.query(models.Pergunta).filter(models.Pergunta.id == pergunta_id).first()
    if not pergunta:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada")
    
    for campo, valor in dados.model_dump().items():
        setattr(pergunta, campo, valor)

    db.commit()
    db.refresh(pergunta)
    return pergunta


# 🔹 Deletar uma pergunta
@router.delete("/{pergunta_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_pergunta(pergunta_id: int, db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(so_admins)):
    pergunta = db.query(models.Pergunta).filter(models.Pergunta.id == pergunta_id).first()
    if not pergunta:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada")

    db.delete(pergunta)
    db.commit()
    return
