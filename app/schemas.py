from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Literal, Optional, List
from app.models import RoleEnum

# ========= USUÁRIO ==========
# Login
class LoginInput(BaseModel):
    email: str
    senha: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str

# Usuário
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioResponse(UsuarioBase):
    id: int
    role: RoleEnum

    model_config = ConfigDict(from_attributes=True)

# ========= QUIZZ ==========
class QuizzBase(BaseModel):
    titulo: str
    descricao: Optional[str]
    categoria: Optional[str]

class QuizzCreate(QuizzBase):
    pass

class QuizzResponse(QuizzBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

        
