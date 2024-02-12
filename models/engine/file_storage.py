#!/bin/usr/python3
"""A class that  serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
from pathlib import Path
from models.user import User

class FileStorage:

    """ A class that  serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key
        <obj class name>.id
        """

        obj_name = obj.__class__.__name__
        key = f"{obj_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON
        file (path: __file_path)"""
        copy_objects = FileStorage.__objects
        dict_objs = {}

        for key in copy_objects.keys():
            dict_objs[key] = copy_objects[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict_objs, f)
        
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
