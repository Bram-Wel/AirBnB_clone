#!/usr/bin/python3
"""The module contains a review class."""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class.

    Args:
        @BaseModel: Supeclass
    Attributes:
        place_id (str): Place ID ::Place.id
        user_id (str): User ID ::User.id
        text (str): The review string
    """
    place_id = ""
    user_id = ""
    text = ""
