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

