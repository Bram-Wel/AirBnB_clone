#!/usr/bin/python3
"""Test classes for FileStorage class."""


import os
import json
import unittest

from datetime import datetime

from models.base_model import BaseModel
from models import storage


class FileStorageTestCase(unittest.TestCase):
    """Test Case for FileStorage class."""

    def setUp(self):
        """Initialise test objects."""
        self.all_objs = storage.all()
        self.obj_base = BaseModel()
        self.fs = storage

    def tearDown(self):
        """Destroy test objects."""
        del self.obj_base
        del self.all_objs
        del self.fs

    def test_save(self):
        """Test that objects are saved to file."""
        self.obj_base.save()
        file = self.fs._FileStorage__file_path
        self.assertTrue(os.path.exists(file))
        self.assertIn(self.obj_base, self.all_objs.values())
        if os.path.exists(file):
            with open(file, 'r+', encoding='utf-8') as fil:
                temp = json.load(fil)
                self.assertIsInstance(temp, dict)
                self.assertIn(self.obj_base.to_dict(), temp.values())
        temp = self.obj_base.updated_at
        self.obj_base = BaseModel(**self.obj_base.to_dict())
        self.assertEqual(temp, self.obj_base.updated_at)
        self.obj_temp = BaseModel()
        self.obj_base = BaseModel(**self.obj_temp.to_dict())
        self.assertLess(temp, self.obj_base.updated_at)
        self.assertEqual(self.obj_temp.updated_at, self.obj_base.updated_at)
        self.obj_base.save()
        self.assertIsInstance(self.obj_base.updated_at, datetime)
        self.assertGreater(self.obj_base.updated_at, self.obj_temp.updated_at)

    def test__file_path(self):
        """Test the FileStorage._FileStorage__file_path variable."""
        self.obj_base.save()
        self.assertIsInstance(self.fs._FileStorage__file_path, str)
        self.assertEqual(self.fs._FileStorage__file_path,
                         'file.json')

    def test__objects(self):
        """Test the FileStorage._FileStorage__objects variable."""
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

    def test_reload(self):
        """Test reloading objects from file."""
        self.obj_base.save()
        self.fs._FileStorage__objects.clear()
        self.assertEqual(self.fs._FileStorage__objects, {})
        self.fs.reload()
        self.assertIn(self.obj_base.to_dict(),
                      [i.to_dict() for i in self.all_objs.values()])
