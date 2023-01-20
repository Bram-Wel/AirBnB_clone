#!/usr/bin/python3
"""This module describes a user class: User."""


from models.base_model import BaseModel


class User(BaseModel):
    """The User Class.

    Args:
        @BaseModel (BaseModel): BaseModel super class

    Attributes:
        email (str): User email
        password (str): User password
        first_name (str): User's First Name
        last_name (str): User's Last Name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, arg):
    #    super(User, self).__init__()
    #    self.arg = arg
