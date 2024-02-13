#!/usr/bin/python3
"""
    base model module
"""
from base_model import BaseModel

class User(BaseModel):
    """
     class User model which is meant for creating Users
    """
    email = str()
    password = str()
    first_name = str()
    last_name = str()
