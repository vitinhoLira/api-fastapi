# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine
from .routes import quizzes
import os

app = FastAPI()

print("URL do banco carregada:", os.getenv("DATABASE_URL"))


Base.metadata.create_all(bind=engine)

app.include_router(quizzes.router)

@app.get("/")
def read_root():
    return {"message": "API FastAPI está no ar 🚀"}
