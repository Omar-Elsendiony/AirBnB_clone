#!/usr/bin/python3
import json
import uuid
import datetime

class FileStorage:
    def __init__(self) -> None:
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        if (obj is not None):
            className = obj.__class__.__name__
            storeDict = obj.__dict__
            storeDict.update({"__class__": className})
            if (obj.id):
                self.__objects[className + "." + obj.id] = storeDict
            else:
                raise AttributeError("object does not have id attribute")
        else:
            raise TypeError("object can not be None")
        

    def save(self):
        try:
            with open(self.__file_path, "w+") as outfile:
                json.dump(self.__objects, outfile, indent=4, sort_keys=True, default=str)
        except FileNotFoundError:
            # print(f"File '{self.__file_path}' not found.")
            pass
    
    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except Exception as E:
            pass
