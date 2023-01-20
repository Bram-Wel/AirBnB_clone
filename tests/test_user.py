#!/usr/bin/python3
"""Test Case classes for the user module."""


import unittest
from datetime import datetime

from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """Test class for the User test cases."""

    def setUp(self):
        """Create class instances."""
        self.obj1 = User()
        self.fs = storage
        self.all_objects = self.fs.all()

    def tearDown(self):
        """Destroy class instances"""
        del self.obj1

    def test_init(self):
        """Test initiaisatin of user objects."""
        self.assertIsNotNone(self.obj1.id)
        self.assertIsNotNone(self.obj1.created_at)
        self.assertIsNotNone(self.obj1.updated_at)
        self.assertIsInstance(self.obj1.id, str)
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime)
        self.assertIsInstance(self.obj1.email, str)
        self.assertIsInstance(self.obj1.first_name, str)
        self.assertIsInstance(self.obj1.last_name, str)
        self.assertIsInstance(self.obj1.password, str)

    def test_attributes(self):
        """Test setting and retrieving attributes."""
        setattr(self.obj1, "email", "airbnb@mail.com")
        setattr(self.obj1, "first_name", "Betty")
        setattr(self.obj1, "last_name", "Bar")
        setattr(self.obj1, "password", "root")
        self.assertEqual("airbnb@mail.com", getattr(self.obj1, "email"))
        self.assertEqual("Betty", getattr(self.obj1, "first_name"))
        self.assertEqual("Bar", getattr(self.obj1, "last_name"))
        self.assertEqual("root", getattr(self.obj1, "password"))

    def test_save(self):
        """Test that set attributes are saved."""
        self.obj1.save()
        self.fs.reload()
        self.assertIn(self.obj1.to_dict(),
                      [i.to_dict() for i in self.all_objects.values()])
