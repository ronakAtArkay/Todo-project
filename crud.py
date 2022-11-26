from sqlalchemy.orm import Session
import models, schemas
from libs import generate_id, time
from fastapi import HTTPException, status

# create a user
def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(id = generate_id(), name = user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# get user by name
def get_name(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.name == user_name).first()

# get all users
def get_users(db: Session, skip : int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# get user by id
def get_names(db: Session, user_id : str):
    return db.query(models.User).filter(models.User.id == user_id).first()


#  update a user
def update(db: Session, id: str, user_name : schemas.UserBase):
    db_user = db.query(models.User).filter(models.User.id== id).first()
    if db_user is None:
        raise HTTPException(status_code= 404, detail="User not Found")
    db_user.name = user_name.name
    db_user.update_at = time()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# permanent delete a user
def delete_user(db: Session, id : str):
    db_user = db.query(models.User).filter(models.User.id == id).delete()
    if db_user is None:
        raise HTTPException(status_code= 404, detail="User not Found")
    db.commit()
    return db_user

# delete user but change only status
def status_change(db: Session, id: str, ):
    db_user = db.query(models.User).filter(models.User.id == id, models.User.is_deleted == False).first()
    if db_user is None:
        raise HTTPException(status_code= 404, detail="User not Found")
    db_user.is_deleted = True
    db_user.update_at = time()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
