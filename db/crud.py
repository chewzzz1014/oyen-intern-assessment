# crud db
from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# TODO: check password matched. hash password

def create_user(db: Session, user: schemas.UserCreateSchema, hashed_password):
    created_user = models.User(username=user.username, password=hashed_password)
    db.add(created_user)
    db.commit()
    db.refresh(created_user)