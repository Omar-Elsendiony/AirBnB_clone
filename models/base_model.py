#!/usr/bin/python3
import uuid
import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        if (kwargs):
            datetimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        dateValue = datetime.datetime.strptime(value, datetimeFormat)
                        setattr(self, key, dateValue)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
    
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
