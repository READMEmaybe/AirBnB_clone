#!/usr/bin/python3
"""Unittest module for the Place Class."""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_attributes(self):
        """Test the creation of Place attributes."""
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_city_id_attribute(self):
        """Test the 'city_id' attribute of Place."""
        place = Place()
        place.city_id = "City123"
        self.assertEqual(place.city_id, "City123")

    def test_user_id_attribute(self):
        """Test the 'user_id' attribute of Place."""
        place = Place()
        place.user_id = "User456"
        self.assertEqual(place.user_id, "User456")

    def test_name_attribute(self):
        """Test the 'name' attribute of Place."""
        place = Place()
        place.name = "Cozy Cabin"
        self.assertEqual(place.name, "Cozy Cabin")

    def test_description_attribute(self):
        """Test the 'description' attribute of Place."""
        place = Place()
        place.description = "A lovely place to relax."
        self.assertEqual(place.description, "A lovely place to relax.")

if __name__ == '__main__':
    unittest.main()
