from sqlalchemy.orm import Session
from . import models


def create_user(db: Session, name: str):
    #cree un objet user avec le nom que lutilisateur vas fournir
    db_user = models.User(name=name)

    #on ajoute cet objet user la
    db.add(db_user)

    db.commit()

    #on recupere lid genere automatiquement
    db.refresh(db_user)

    return db_user



def get_user(db: Session, user_id:int):
    #recupere un user pas son id

    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    #recupere la liste des utilisateurs
    #list = combien dutilisateurs on vas sauter pour la pagination 
    #limit = combien dutilisateurs maximum

    return db.query(models.User).offset(skip).limit(limit).all()


def create_subject(db: Session, user_id:int, name:str):
    db_subject = models.Subject(name = name, user_id=user_id)

    db.add(db_subject)

    db.commit()

    db.refresh(db_subject)

    return db_subject



def get_subject(db: Session, subject_id: int):
    """une matière par son id"""
    return db.query(models.Subject).filter(models.Subject.id == subject_id).first()


def get_subject_by_user(db: Session, user_id:int):
    """toutes les matières d'un utilisateur"""
    return db.query(models.Subject).filter(models.Subject.user_id == user_id).first()


def get_subjects(db: Session, skip: int = 0, limit: int = 100):
    """toutes les matières"""
    return db.query(models.Subject).offset(skip).limit(limit).all()
