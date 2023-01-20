#!/usr/bin/python3
"""The module describes a city class."""


from models.base_model import BaseModel


class City(BaseModel):
    """The City Class.

    Args:
        @BaseModel (BaseModel): BaseModel super class
    Attributes:
        state_id (str): State ID ::State.id
        name (str): City Name
    """
    state_id = ""
    name = ""
