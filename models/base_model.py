#!/usr/bin/python3
from typing import Any
import uuid
import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        # self.updated_at = None
        if (kwargs):
            datetimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        dateValue = datetime.datetime.strptime(value, datetimeFormat)
                        setattr(self, "__" + key, dateValue)
                    else:
                        setattr(self, "__" + key, value)
        else:
            self.__id = str(uuid.uuid4())
            todayDate = datetime.datetime.now()
            self.created_at = todayDate.isoformat()
            self.updated_at = todayDate.isoformat()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, time):
        self.__updated_at = time

    @property
    def created_at(self):
        return self.__updated_at
    
    @created_at.setter
    def created_at(self, time):
        self.__created_at = time

    def __str__(self):
        return f'{self.__class__.__name__} {self.id} {self.__dict__}'

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dictionaryToBeReturned = self.__dict__
        dictionaryToBeReturned.update({"class": self.__class__.__name__})
        dictionaryToBeReturned.update({"created_at": datetime.datetime.isoformat(self.created_at)})
        dictionaryToBeReturned.update({"updated_at": datetime.datetime.isoformat(self.updated_at)})
        return dictionaryToBeReturned

# b = BaseModel()
# b.__str__()
# print(b.to_dict())
