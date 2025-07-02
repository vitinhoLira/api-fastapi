from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(
    prefix="/resultados",
    tags=["Resultados"]
)

# 🔹 Criar novo resultado
@router.post("/", response_model=schemas.ResultadoResponse)
def criar_resultado(resultado: schemas.ResultadoCreate, db: Session = Depends(get_db)):
    quizz = db.query(models.Quizz).filter(models.Quizz.id == resultado.quizz_id).first()
    if not quizz:
        raise HTTPException(status_code=404, detail="Quizz não encontrado")

    usuario = db.query(models.Usuario).filter(models.Usuario.id == resultado.user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    novo_resultado = models.Resultado(**resultado.model_dump())
    db.add(novo_resultado)
    db.commit()
    db.refresh(novo_resultado)
    return novo_resultado


# 🔹 Listar todos os resultados
@router.get("/", response_model=list[schemas.ResultadoResponse])
def listar_resultados(db: Session = Depends(get_db)):
    return db.query(models.Resultado).all()


# 🔹 Buscar resultado por ID
@router.get("/{resultado_id}", response_model=schemas.ResultadoResponse)
def buscar_resultado(resultado_id: int, db: Session = Depends(get_db)):
    resultado = db.query(models.Resultado).filter(models.Resultado.id == resultado_id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado não encontrado")
    return resultado


# 🔹 Deletar resultado
@router.delete("/{resultado_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_resultado(resultado_id: int, db: Session = Depends(get_db)):
    resultado = db.query(models.Resultado).filter(models.Resultado.id == resultado_id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado não encontrado")

    db.delete(resultado)
    db.commit()
    return
