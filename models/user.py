#!/usr/bin/python3
"""
    user model module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
     class User model which is meant for creating Users
    """
    email = str()
    password = str()
    first_name = str()
    last_name = str()
