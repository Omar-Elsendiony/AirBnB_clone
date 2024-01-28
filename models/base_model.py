#!/usr/bin/python3
"""
    base model module
"""
from typing import Any
import uuid
import datetime
from __init__ import storage


class BaseModel:
    """
     class base model which is the fundamental class for nosr of the logic
    """
    def __init__(self, *args, **kwargs):
        # self.updated_at = None
        if (kwargs):
            datetimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        dateValue = datetime.datetime.\
                            strptime(value, datetimeFormat)
                        setattr(self, key, dateValue)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            todayDate = datetime.datetime.now().isoformat()
            self.created_at = todayDate
            self.updated_at = todayDate
            storage.new(self)


    def __str__(self):
        className = self.__class__.__name__
        return f'[{className}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()
        storage.save()


    def to_dict(self):
        d1 = {}
        d1.update(self.__dict__)
        d1.update({"__class__": self.__class__.__name__})
        return d1

