#!/usr/bin/python3
from models.user import User
from models.base_model import BaseModel

u = User()
print(isinstance(u, BaseModel))
