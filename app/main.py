# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal

app = FastAPI()

# Dependency para obter o DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API FastAPI está no ar 🚀"}
