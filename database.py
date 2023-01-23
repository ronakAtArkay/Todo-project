from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqlalchemy_database_url = "sqlite:///./sql_app.db"
sqlalchemy_database_url = (
    "mysql+mysqlconnector://root:%s@localhost:3306/todo_db" % quote("Arkay@210")
)

engin = create_engine(sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base = declarative_base()
