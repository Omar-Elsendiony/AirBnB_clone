#!/usr/bin/python3
import json
import os
import sys
# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# sys.path.append(parent)
from models.base_model import BaseModel


class FileStorage:
    def __init__(self) -> None:
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        if (obj is not None):
            className = obj.__class__.__name__
            # storeDict = obj.__dict__
            # storeDict.update({"__class__": className})
            # storeDict = obj.to_dict()
            if (obj.id):
                self.__objects[className + "." + obj.id] = obj
            else:
                raise AttributeError("object does not have id attribute")
        else:
            raise TypeError("object can not be None")
        

    def save(self):
        try:
            dictObj = {}
            for objID, objVal in self.__objects.items():
                dictObj[objID] = objVal.to_dict()
            with open(self.__file_path, "w") as outfile:
                json.dump(dictObj, outfile)
        except FileNotFoundError:
            # print(f"File '{self.__file_path}' not found.")
            pass
    
    def reload(self):
        try:     
            with open(self.__file_path, "r") as file:
                dictionaries = json.load(file)
                for key, value in dictionaries.items():
                    split_ = key.split('.')
                    classname = split_[0]
                    id_ = split_[1]
                    self.__objects[classname + "." + id_] = globals()[classname](**value)

        except Exception as E:
            pass
