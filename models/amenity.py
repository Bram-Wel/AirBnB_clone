#!/usr/bin/python3
"""The module contains an amenity class."""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class.

    Args:
        @BaseModel: Supeclass
    Attributes:
        name (str): Amenity
    """
    name = ""
