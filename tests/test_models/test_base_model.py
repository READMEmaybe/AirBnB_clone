#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def test_instantiation(self):
        """Tests instantiation of BaseModel class."""

        new = BaseModel()
        self.assertIsInstance(new, BaseModel)
        self.assertIs(type(new), BaseModel)
        self.assertEqual(str(type(new)), "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(new), BaseModel))
        new.name = "( ͡° ͜ʖ ͡°)"
        new.my_number = 13
        self.assertEqual(new.name, "( ͡° ͜ʖ ͡°)")
        self.assertEqual(new.my_number, 13)

    def test_attributes(self):
        """Test the creation of BaseModel attributes."""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)

    def test_id_generation(self):
        """Test if the 'id' attribute is a string."""
        obj = BaseModel()
        self.assertEqual(type(obj.id), str)

    def test_to_dict(self):
        """Test the to_dict method."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_save(self):
        """Test the save method."""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_str_representation(self):
        """Test the __str__ method."""
        obj = BaseModel()
        obj_str = str(obj)
        self.assertTrue(obj.__class__.__name__ in obj_str)
        self.assertTrue(obj.id in obj_str)
        self.assertTrue(str(obj.__dict__) in obj_str)



if __name__ == '__main__':
    unittest.main()
