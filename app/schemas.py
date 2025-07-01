from pydantic import BaseModel, EmailStr
from typing import Optional, List
from enum import Enum

# ======== ENUM para papel do usuário ==========
class RoleEnum(str, Enum):
    usuario = "usuario"
    admin = "admin"

# ========= USUÁRIO ==========
class UsuarioBase(BaseModel):
    nome: Optional[str]
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str  # campo de entrada

class UsuarioResponse(UsuarioBase):
    id: int
    role: RoleEnum

    class Config:
        orm_mode = True

# ========= QUIZZ ==========
class QuizzBase(BaseModel):
    titulo: str
    descricao: Optional[str]
    categoria: Optional[str]

class QuizzCreate(QuizzBase):
    pass

class QuizzResponse(QuizzBase):
    id: int

    class Config:
        orm_mode = True

# ========= PERGUNTA ==========
class PerguntaBase(BaseModel):
    enunciado: str
    alternativa1: str
    alternativa2: str
    alternativa3: str
    alternativa4: str
    respCorreta: str

class PerguntaCreate(PerguntaBase):
    quizz_id: int

class PerguntaResponse(PerguntaBase):
    id: int
    quizz_id: int

    class Config:
        orm_mode = True

# ========= RESULTADO ==========
class ResultadoBase(BaseModel):
    pontuacao: int
    acertos: int
    erros: int

class ResultadoCreate(ResultadoBase):
    quizz_id: int
    user_id: int

class ResultadoResponse(ResultadoBase):
    id: int
    quizz_id: int
    user_id: int

    class Config:
        orm_mode = True
