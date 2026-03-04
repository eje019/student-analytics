from fastapi import FastAPI
from .database import engine
from . import models

# Crée les tables dans PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Analytics API")

@app.get("/")
def root():
    return {"message": "API Student Analytics"}

@app.get("/test")
def test():
    return {"resultat": "Ceci est un test"}