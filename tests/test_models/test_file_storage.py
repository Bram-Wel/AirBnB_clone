#!/usr/bin/python3
"""Test classes for FileStorage class."""


import os
import json
import unittest

from models.base_model import BaseModel
from models import storage


class FileStorageTestCase(unittest.TestCase):
    """Test Case for FileStorage class."""

    def setUp(self):
        """Initialise test objects."""
        self.all_objs = storage.all()
        self.obj_base = BaseModel()

    def tearDown(self):
        """Destroy test objects."""
        del self.obj_base
        del self.all_objs

    def test_save(self):
        """Test that objects are saved to file."""
        self.obj_base.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertIn(self.obj_base, self.all_objs.values())
        if os.path.exists('file.json'):
            with open('file.json', 'r+', encoding='utf-8') as file:
                temp = json.load(file)
                self.assertIsInstance(temp, dict)
                self.assertIn(self.obj_base.to_dict(), temp.values())
