import schemas
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
from libs import generate_id, now


# create a todo
def create_todo(db: Session, todo: schemas.TodoBase):
    db_todo = models.TodoModel(id=generate_id(), name=todo.name)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todo_by_id(db: Session, todo_id : str):
    return db.query(models.TodoModel).filter(models.TodoModel.id == todo_id, models.TodoModel.is_deleted == False).first()


# get todo by name
def get_todo(db: Session, todo_id: str):
    db_todo = get_todo_by_id(todo_id=todo_id, db=db)
    if db_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="todo not found")
    return db_todo


# get all todo
def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TodoModel).filter(models.TodoModel.is_deleted == False).offset(skip).limit(limit).all()



#  update a todo
def update_todo(db: Session, todo_id: str, todo_name: schemas.TodoBase):
    db_todo = get_todo_by_id(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="todo not Found")
    db_todo.name = todo_name.name
    db_todo.update_at = now()
    db.commit()
    db.refresh(db_todo)
    return db_todo


# permanent delete a todo
def delete_todo(db: Session, todo_id: str):
    db_todo = get_todo_by_id(todo_id=todo_id, db=db)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="todo not Found")
    db.commit()
    return db_todo


# delete todo but change only status
def status_change(
    db: Session,
    todo_id: str,
):
    db_todo = get_todo_by_id(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="todo not Found")
    db_todo.is_deleted = True
    db_todo.update_at = now()
    db.commit()
    return 
