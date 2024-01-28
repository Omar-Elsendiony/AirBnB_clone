#!/usr/bin/python3
import json
import uuid
import datetime

class FileStorage:
    def __init__(self, filepath) -> None:
        self.__file_path = filepath
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        if (obj is not None):
            className = obj.__class__.__name__
            if (obj.id):
                self.__objects[className + obj.id] = obj.to_dict()
            else:
                raise AttributeError("object does not have id attribute")
        else:
            raise TypeError("object can not be None")
        

    def save(self):
        try:
            with open(self.__file_path, "a") as outfile:
                json.dump(self.__objects, outfile)
        except FileNotFoundError:
            # print(f"File '{self.__file_path}' not found.")
            pass
    
    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
