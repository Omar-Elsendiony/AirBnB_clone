#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if (obj is not None):
            className = obj.__class__.__name__
            if (obj.id):
                FileStorage.__objects[className + "." + obj.id] = obj
            else:
                raise AttributeError("object does not have id attribute")
        else:
            raise TypeError("object can not be None")

    def save(self):
        try:
            dictObj = {}
            for objID, objVal in FileStorage.__objects.items():
                dictObj[objID] = objVal.to_dict()
            with open(FileStorage.__file_path, "w") as outfile:
                json.dump(dictObj, outfile)
        except FileNotFoundError:
            pass

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                dictionaries = json.load(file)
                for key, value in dictionaries.items():
                    split_ = key.split('.')
                    classname = split_[0]
                    id_ = split_[1]
                    FileStorage.__objects[classname + "." + id_] = \
                        globals()[classname](**value)
        except Exception as E:
            pass
