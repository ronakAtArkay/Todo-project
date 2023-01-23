from typing import List
import crud
import schemas
from fastapi import Depends, FastAPI, Path, status
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engin

models.Base.metadata.create_all(bind=engin)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create a todo
@app.post("/todo")
def create_todo(todo: schemas.TodoBase, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)


# search todo by name
@app.get("/todo/{todo_id}", response_model=schemas.TodoDetail)
def get_todo(todo_id: str = Path(..., min_length=36, max_length=36), db: Session = Depends(get_db)):
    data = crud.get_todo(db, todo_id=todo_id)
    return data


# get all todos data
@app.get("/todo",  response_model=List[schemas.TodoDetail])
def get_todos_all_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    data = crud.get_todos(db, skip=skip, limit=limit)
    return data


# update a todo by id
@app.put("/todo/{todo_id}", response_model=schemas.TodoDetail)
def update_todo(todo_name: schemas.TodoBase, todo_id: str= Path(..., min_length=36, max_length=36), db: Session = Depends(get_db)):
    data = crud.update_todo(db, todo_name=todo_name, todo_id=todo_id)
    return data


# delete a todo by id
@app.delete("/todo/{todo_id}")
def delete_todo_data(id: str= Path(..., min_length=36, max_length=36), db: Session = Depends(get_db)):
    data = crud.delete_todo(db, id=id)
    return data


# status change by delete
@app.delete("/todo/{todo_id}/")
def delete_todo_without_data(todo_id: str = Path(..., min_length=36, max_length=36), db: Session = Depends(get_db)):
    data = crud.status_change(db=db, todo_id=todo_id)
    return status.HTTP_204_NO_CONTENT
