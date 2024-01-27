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
                        dateValue = datetime.datetime.\
                            strptime(value, datetimeFormat)
                        setattr(self, "__" + key, dateValue)
                    else:
                        setattr(self, "__" + key, value)
        else:
            self.id = str(uuid.uuid4())
            todayDate = datetime.datetime.now()
            self.created_at = todayDate
            self.updated_at = todayDate

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
        className = self.__class__.__name__
        return f'[{className}] ({self.id}) {self.refinedDictionary()}'

    def save(self):
        self.updated_at = datetime.datetime.now()

    def refinedDictionary(self):
        oldDictionary = self.__dict__
        className = self.__class__.__name__
        d1 = {}

        d1.update({"my_number": oldDictionary.get("my_number")})
        d1.update({"name": oldDictionary.get("name")})
        d1.update({"updated_at": datetime.datetime.isoformat(self.updated_at)})
        d1.update({"id": oldDictionary.get("_{}__id".format(className))})
        d1.update({"created_at": datetime.datetime.isoformat(self.created_at)})
        return d1

    def to_dict(self):
        oldDictionary = self.__dict__
        className = self.__class__.__name__
        d1 = {}

        d1.update({"my_number": oldDictionary.get("my_number")})
        d1.update({"name": oldDictionary.get("name")})
        d1.update({"__class__": className})
        d1.update({"updated_at": datetime.datetime.isoformat(self.updated_at)})
        d1.update({"id": oldDictionary.get("_{}__id".format(className))})
        d1.update({"created_at": datetime.datetime.isoformat(self.created_at)})
        return d1

# b = BaseModel()
# b.__str__()
# print(b.to_dict())
