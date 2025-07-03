from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.auth.dependencies import get_usuario_logado, so_admins
from app.database import get_db

router = APIRouter(prefix="/quizzes", tags=["Quizzes"])

# Criar Quiz
@router.post("/", response_model=schemas.QuizzResponse)
def create_quizz(quizz: schemas.QuizzCreate, db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(so_admins)):
    db_quizz = models.Quizz(**quizz.model_dump())
    db.add(db_quizz)
    db.commit()
    db.refresh(db_quizz)
    return db_quizz

# Listar todos os quizzes
@router.get("/", response_model=list[schemas.QuizzResponse])
def get_quizzes(db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(get_usuario_logado)):
    return db.query(models.Quizz).all()

# Buscar quiz por ID
@router.get("/{quizz_id}", response_model=schemas.QuizzResponse)
def get_quizz(quizz_id: int, db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(get_usuario_logado)):
    quizz = db.query(models.Quizz).filter(models.Quizz.id == quizz_id).first()
    if not quizz:
        raise HTTPException(status_code=404, detail="Quiz não encontrado")
    return quizz

# Atualizar quiz
@router.put("/{quizz_id}", response_model=schemas.QuizzResponse)
def update_quizz(quizz_id: int, updated: schemas.QuizzCreate, db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(so_admins)):
    quizz = db.query(models.Quizz).filter(models.Quizz.id == quizz_id).first()
    if not quizz:
        raise HTTPException(status_code=404, detail="Quiz não encontrado")
    for key, value in updated.model_dump().items():
        setattr(quizz, key, value)
    db.commit()
    db.refresh(quizz)
    return quizz

# Deletar quiz
@router.delete("/{quizz_id}")
def delete_quizz(quizz_id: int, db: Session = Depends(get_db), usuario_logado: models.Usuario = Depends(so_admins)):
    quizz = db.query(models.Quizz).filter(models.Quizz.id == quizz_id).first()
    if not quizz:
        raise HTTPException(status_code=404, detail="Quiz não encontrado")
    db.delete(quizz)
    db.commit()
    return {"message": "Quiz deletado com sucesso"}
