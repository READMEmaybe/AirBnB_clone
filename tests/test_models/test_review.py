#!/usr/bin/python3
"""Unittest module for the Review Class."""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_attributes(self):
        """Test the creation of Review attributes."""
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_place_id_attribute(self):
        """Test the 'place_id' attribute of Review."""
        review = Review()
        review.place_id = "Place123"
        self.assertEqual(review.place_id, "Place123")

    def test_user_id_attribute(self):
        """Test the 'user_id' attribute of Review."""
        review = Review()
        review.user_id = "User456"
        self.assertEqual(review.user_id, "User456")

    def test_text_attribute(self):
        """Test the 'text' attribute of Review."""
        review = Review()
        review.text = "A great experience!"
        self.assertEqual(review.text, "A great experience!")

if __name__ == '__main__':
    unittest.main()
