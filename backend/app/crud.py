from sqlalchemy.orm import Session
from . import models


def create_user(db: Session, name: str):
    db_user = models.User(name=name)

    db.add(db_user)