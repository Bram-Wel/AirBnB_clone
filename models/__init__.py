#!/usr/bin/python3
"""This module initialises the module package."""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
