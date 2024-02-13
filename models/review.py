#!/usr/bin/python3
"""
    place model module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
     class User model which is meant for creating Users
    """
    place_id = str()
    user_id = str()
    text = str()
