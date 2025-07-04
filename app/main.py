# app/main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.routes import perguntas, resultados, quizzes, usuarios
from .database import Base, engine
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # 🔓 Libera tudo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quizzes.router)
app.include_router(perguntas.router)
app.include_router(resultados.router)
app.include_router(usuarios.router)

@app.get("/")
def read_root():
    return {"message": "API FastAPI está no ar 🚀"}
