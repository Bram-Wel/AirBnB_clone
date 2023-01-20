#!/usr/bin/python3
"""Modules contains the a state class."""


from models.base_model import BaseModel


class State(BaseModel):
    """The State Class.

    Args:
        @BaseModel (BaseModel): BaseModel super class
    Attributes:
        name (str): State name
    """

    name = ""
