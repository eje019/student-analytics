from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud 
from ..database import SessionLocal

router = APIRouter()

#depandance pour obtenir la session base de donnees
def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()

@router.post("/subjects")
def create_subject( name:str, user_id: str, db: Session = Depends(get_db())):
    return crud.create_subject(db=db, name=name, user_id=user_id)

@router.get("/subjects")
def read_subjects(skip: int = 0, limit : int = 100, db : Session = Depends(get_db())):
    return crud.get_subjects(db, skip=skip, limit=limit)

@router.get("/subjects/{subject_id}")
def read_subject(subject_id: int, db : Session=Depends(get_db())):
    db_user = crud.get_subject()

    