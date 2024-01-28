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
            todayDate = datetime.datetime.now()
            self.created_at = todayDate
            self.updated_at = todayDate
            storage.new(self)

    # @property
    # def updated_at(self):
    #     return self.updated_at

    # @updated_at.setter
    # def updated_at(self, time):
    #     self.updated_at = time

    # @property
    # def created_at(self):
    #     return self.updated_at

    # @created_at.setter
    # def created_at(self, time):
    #     self.created_at = time

    def __str__(self):
        className = self.__class__.__name__
        return f'[{className}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()


    def to_dict(self):
        oldDictionary = self.__dict__
        className = self.__class__.__name__
        d1 = {}

        d1.update({"my_number": oldDictionary.get("my_number")})
        d1.update({"name": oldDictionary.get("name")})
        d1.update({"__class__": className})
        d1.update({"updated_at": self.updated_at.isoformat()})
        d1.update({"id": oldDictionary.get("id")})
        d1.update({"created_at": self.created_at.isoformat()})
        return d1

# b = BaseModel()
# b.__str__()
# print(b.to_dict())
