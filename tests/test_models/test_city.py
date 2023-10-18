#!/usr/bin/python3
"""Unittest module for the City Class."""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_attributes(self):
        """Test the creation of City attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_state_id_attribute(self):
        """Test the 'state_id' attribute of City."""
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_name_attribute(self):
        """Test the 'name' attribute of City."""
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

if __name__ == '__main__':
    unittest.main()
