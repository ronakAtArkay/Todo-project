from typing import List
from fastapi import FastAPI, Depends, Body, status, HTTPException
import models, schemas, crud
from database import engin, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engin)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create a user
@app.post("/users/")
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db = db, user=user)

# search user by name
@app.get("/users/{user_name}", response_model=schemas.UserBase)
def read_user(user_name = str,  db : Session = Depends(get_db)):
    users = crud.get_name(db, user_name = user_name)
    if users is None:
        raise HTTPException(status_code= 404, detail="User not Found")
    return users

# get all users data
@app.get("/users/", response_model= List[schemas.UserBase])
def read_users(skip : int = 0, limit : int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit= limit)
    return users


# search user by id
@app.get("/users/{user_id}/")
def all_user(user_id, db: Session = Depends(get_db)):
    users = crud.get_names(db, user_id)
    if users is None:
        raise HTTPException(status_code= 404, detail="User not Found")
    return users

# update a user by id
@app.put("/users/{id}")
def update(user_name : schemas.UserBase, id : str,  db: Session = Depends(get_db)):
    users =  crud.update(db, user_name = user_name, id=id)
    return users

# delete a user by id
@app.delete("/users/{id}")
def delete_user(id : str, db: Session = Depends(get_db)):
    users = crud.delete_user(db, id=id)
    return users

# status change by delete
@app.delete("/users/{id}/")
def status_changed(id : str, db: Session = Depends(get_db)):
    users = crud.status_change(db, id = id)
    return users

