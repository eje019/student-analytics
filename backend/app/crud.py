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



def read_user(db: Session, user_id:int):
    #recupere un user pas son id

    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    #recupere la liste des utilisateurs
    #list = combien dutilisateurs on vas sauter pour la pagination 
    #limit = combien dutilisateurs maximum

    return db.query(models.User).offset(skip).limit(limit).all()
