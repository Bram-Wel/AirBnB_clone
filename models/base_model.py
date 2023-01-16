#!/usr/bin/python3
"""This module describes a base class: BaseModel."""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Define & manage common attributes and methods for subclasses.

    Attributes:
        id (str): uuid string
        created_at (datetime): Creation datetime for class instance
        updated_at (datetime): datetime when instance is updated
    """

    def __init__(self, **kwargs):
        """Initialise the object instance."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary of writable instance attributes."""
        attr_dict = {i: self.__dict__[i] for i in self.__dict__}
        attr_dict.update({"__class__": self.__class__.__name__})
        attr_dict.update({key: attr_dict[key].isoformat() for key in attr_dict
                          if isinstance(attr_dict[key], datetime)})
        return attr_dict

    def __str__(self):
        """Return a string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
