#!/usr/bin/python3
"""
    place model module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
     class User model which is meant for creating Users
    """
    city_id = str()
    user_id = str()
    name = str()
    description = str()
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = (float)(0.0)
    longitude = (float)(0.0)
    amenity_ids = list(str())
