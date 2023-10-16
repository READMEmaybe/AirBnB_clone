#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        """Test the 'all' method when no objects are stored."""
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

    def test_new(self):
        """Test the 'new' method."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertIn(key, objects)

    def test_save_and_reload(self):
        """Test the 'save' and 'reload' methods."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn(key, objects)


if __name__ == '__main__':
    unittest.main()
