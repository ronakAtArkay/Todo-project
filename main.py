from fastapi import FastAPI, Depends, HTTPException
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


# create a todo
@app.post("/todo/")
def create_todo(todo: schemas.TodoBase, db: Session = Depends(get_db)):
    return crud.create_todo(db = db, todo=todo)

# search todo by name
@app.get("/todo/{todo_name}", response_model=schemas.TodoDetail)
def get_todo_by_name(todo_name : str, db : Session = Depends(get_db)):
    todos = crud.get_name(db, todo_name = todo_name)
    if todos is None:
        raise HTTPException(status_code= 404, detail="todo not Found")
    return todos

# get all todos data
@app.get("/todo")
def get_todos_all_data(skip : int = 0, limit : int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit= limit)
    return todos


# search todo by id
@app.get("/todo/{todo_id}/", response_model=schemas.TodoDetail)
def get_todo_by_id(todo_id, db: Session = Depends(get_db)):
    todos = crud.get_name_by_id(db, todo_id)
    if todos is None:
        raise HTTPException(status_code= 404, detail="todo not Found")
    return todos

# update a todo by id
@app.put("/todo/{id}", response_model=schemas.TodoDetail)
def update_todo(todo_name : schemas.TodoBase, id : str,  db: Session = Depends(get_db)):
    users =  crud.update(db, todo_name = todo_name, id=id)
    return users

# delete a todo by id
@app.delete("/todo/{id}")
def delete_todo_data(id : str, db: Session = Depends(get_db)):
    todos = crud.delete_todo(db, id=id)
    return todos

# status change by delete
@app.delete("/todo/{id}/")
def delete_todo_without_data(id : str, db: Session = Depends(get_db)):
    todos = crud.status_change(db, id = id)
    return todos

