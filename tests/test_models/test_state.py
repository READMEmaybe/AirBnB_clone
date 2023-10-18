#!/usr/bin/python3
"""Unittest module for the State Class."""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_attributes(self):
        """Test the creation of State attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_name_attribute(self):
        """Test the 'name' attribute of State."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

if __name__ == '__main__':
    unittest.main()
