from sqlalchemy.orm import Session
import models, schemas
from libs import generate_id, time
from fastapi import HTTPException

# create a todo
def create_todo(db: Session, todo: schemas.TodoBase):
    db_todo = models.Todo(id = generate_id(), name = todo.name)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# get todo by name
def get_name(db: Session, todo_name: str):
    return db.query(models.Todo).filter(models.Todo.name == todo_name).first()

# get all todo
def get_todos(db: Session, skip : int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

# get todo by id
def get_name_by_id(db: Session, todo_id : str):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


#  update a todo
def update(db: Session, id: str, todo_name : schemas.TodoBase):
    db_todo = db.query(models.Todo).filter(models.Todo.id== id).first()
    if db_todo is None:
        raise HTTPException(status_code= 404, detail="todo not Found")
    db_todo.name = todo_name.name
    db_todo.update_at = time()
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# permanent delete a todo
def delete_todo(db: Session, id : str):
    db_todo = db.query(models.Todo).filter(models.Todo.id == id).delete()
    if db_todo is None:
        raise HTTPException(status_code= 404, detail="todo not Found")
    db.commit()
    return db_todo

# delete todo but change only status
def status_change(db: Session, id: str, ):
    db_todo = db.query(models.Todo).filter(models.Todo.id == id, models.Todo.is_deleted == False).first()
    if db_todo is None:
        raise HTTPException(status_code= 404, detail="todo not Found")
    db_todo.is_deleted = True
    db_todo.update_at = time()
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
