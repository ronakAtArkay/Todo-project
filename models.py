from sqlalchemy import Boolean,Column, String, DateTime
from database import Base
from datetime import datetime

class User(Base):
    __tablename__= "users"

    id = Column(String(200), primary_key = True)
    name = Column(String(200), unique = True)
    is_completed = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.now)
    update_at = Column(DateTime, default = datetime.now)
    is_deleted = Column(Boolean, default = False)
    