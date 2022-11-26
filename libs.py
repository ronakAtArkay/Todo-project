from uuid import uuid4
from datetime import datetime

# def genrate_id():
#     u_id = uuid.uuid4()
#     return u_id

def generate_id():
    id = str(uuid4())
    return id

def time():
    return datetime.now()