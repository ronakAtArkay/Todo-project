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
@app.post("/todo/")
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db = db, user=user)

# search user by name
@app.get("/todo/{user_name}", response_model=schemas.UserDetail)
def get_user_by_name(user_name : str, db : Session = Depends(get_db)):
    users = crud.get_name(db, user_name = user_name)
    if users is None:
        raise HTTPException(status_code= 404, detail="User not Found")
    return users

# get all users data
@app.get("/todo/", response_model=schemas.UserDetail)
def get_todos_all_data(skip : int = 0, limit : int = 100, db: Session = Depends(get_db)):
    users = crud.get_todos(db, skip=skip, limit= limit)
    return users


# search user by id
@app.get("/todo/{user_id}/", response_model=schemas.UserDetail)
def get_todo_by_id(user_id, db: Session = Depends(get_db)):
    users = crud.get_name_by_id(db, user_id)
    if users is None:
        raise HTTPException(status_code= 404, detail="User not Found")
    return users

# update a user by id
@app.put("/todo/{id}", response_model=schemas.UserDetail)
def update_todo(user_name : schemas.UserBase, id : str,  db: Session = Depends(get_db)):
    users =  crud.update(db, user_name = user_name, id=id)
    return users

# delete a user by id
@app.delete("/todo/{id}")
def delete_todo_data(id : str, db: Session = Depends(get_db)):
    users = crud.delete_todo(db, id=id)
    return users

# status change by delete
@app.delete("/todo/{id}/")
def delete_todo_without_data(id : str, db: Session = Depends(get_db)):
    users = crud.status_change(db, id = id)
    return users

