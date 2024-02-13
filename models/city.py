#!/usr/bin/python3
"""
    City model module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
     class City model which is meant for creating Users
    """
    state_id = str()
    name = str()
