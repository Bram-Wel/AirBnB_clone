#!/usr/bin/python3
"""This module describes TestCase classes for our
base_model module.
"""


import unittest
import uuid

from datetime import datetime

from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):
    """A test case for BaseModel Class."""

    def setUp(self):
        """Create class instances."""
        self.obj1 = BaseModel()

    def tearDown(self):
        """Destroy instances after tests."""
        del self.obj1

    def test_init(self):
        """Test initialisation of the object(s)."""
        self.assertIsNotNone(self.obj1.id)
        self.assertIsNotNone(self.obj1.created_at)
        self.assertIsNotNone(self.obj1.updated_at)
        with self.assertRaises(AssertionError):
            self.assertIsInstance(self.obj1.id, uuid.UUID)
        self.assertIsInstance(self.obj1.id, str)
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime)
        self.assertEqual(self.obj1.created_at, self.obj1.updated_at)

        self.obj1.name = "My First Model"
        self.obj1.my_number = 89
        self.assertEqual(self.obj1.name, "My First Model")
        self.assertEqual(self.obj1.my_number, 89)
        self.obj1.save()
        self.assertNotEqual(self.obj1.created_at, self.obj1.updated_at)

        self.assertIsInstance(self.obj1.to_dict(), dict)
        self.assertIn('id', self.obj1.to_dict())
        self.assertIn('created_at', self.obj1.to_dict())
        self.assertIn('updated_at', self.obj1.to_dict())
        self.assertIn('name', self.obj1.to_dict())
        self.assertIn('my_number', self.obj1.to_dict())
        self.assertIsInstance(self.obj1.to_dict()['created_at'], str)
        self.assertIsInstance(self.obj1.to_dict()['updated_at'], str)
