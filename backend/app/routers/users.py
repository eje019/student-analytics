from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud
from ..database import SessionLocal

router = APIRouter()

#dependance pour obtenir la session base de donnees 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def create_user(name: str, db: Session = Depends(get_db)):
    """endpoint pour créer un utilisateur"""
    return crud.create_user(db=db, name=name)


@router.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Endpoint pour lister les utilisateurs
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer un utilisateur par son id
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return db_user

