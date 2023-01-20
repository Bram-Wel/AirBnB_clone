#!/usr/bin/python3
"""This module describes an object serialisation/deserialisation
class.
"""


import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Serialise class instances to a JSON file and vice versa.

    Attributes:
        file_path (str): Path to JSON file
        objects (dict): Store objects
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Insert the object in __objects dictionary.

        Args:
            obj (object): Object instance
        """
        FileStorage.__objects.update({
                                    f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """Serialise objects to file in file_path."""
        temp = FileStorage.__objects.copy()
        temp.update({i: temp[i].to_dict() for i in temp})
        with open(FileStorage.__file_path, 'w+', encoding='utf-8') as file:
            json.dump(temp, file)

    def reload(self):
        """Deserialise JSON file to objects dictionary."""
        try:
            temp = None
            with open(FileStorage.__file_path, 'r+', encoding='utf-8') as file:
                temp = json.load(file)
            for i in temp.values():
                self.new(eval(i['__class__'])(**i))
        except OSError:
            pass
