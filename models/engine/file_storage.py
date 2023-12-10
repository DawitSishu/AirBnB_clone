#!/usr/bin/python3
"""
a filestorage to store data
"""

import json
from models.base_model import BaseModel
import datetime
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    main filestorage engine class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets the dictionary object id."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """sterilize object to json"""
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            new_d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_d, file)

    def reload(self):
        """deserilizes the json if it exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
