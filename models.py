from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String

from database import Base


class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(String(200), primary_key=True)
    name = Column(String(200))
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now)
    is_deleted = Column(Boolean, default=False)
