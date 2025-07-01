# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum

class RoleEnum(enum.Enum):
    usuario = "usuario"
    admin = "admin"

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, nullable=False, index=True)
    senha = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.usuario)

    resultados = relationship("Resultado", back_populates="usuario", cascade="all, delete", passive_deletes=True)


class Quizz(Base):
    __tablename__ = "quizz"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String)
    categoria = Column(String)

    perguntas = relationship("Pergunta", back_populates="quizz", cascade="all, delete", passive_deletes=True)
    resultados = relationship("Resultado", back_populates="quizz", cascade="all, delete", passive_deletes=True)


class Pergunta(Base):
    __tablename__ = "pergunta"

    id = Column(Integer, primary_key=True, index=True)
    enunciado = Column(String)
    alternativa1 = Column(String)
    alternativa2 = Column(String)
    alternativa3 = Column(String)
    alternativa4 = Column(String)
    respCorreta = Column(String)

    quizz_id = Column(Integer, ForeignKey("quizz.id", ondelete="CASCADE"), nullable=False)

    quizz = relationship("Quizz", back_populates="perguntas")


class Resultado(Base):
    __tablename__ = "resultado"

    id = Column(Integer, primary_key=True, index=True)
    pontuacao = Column(Integer)
    acertos = Column(Integer)
    erros = Column(Integer)

    quizz_id = Column(Integer, ForeignKey("quizz.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False)

    quizz = relationship("Quizz", back_populates="resultados")
    usuario = relationship("Usuario", back_populates="resultados")
