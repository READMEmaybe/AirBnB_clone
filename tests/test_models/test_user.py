#!/usr/bin/python3
"""Unittest module for the User Class."""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_attributes(self):
        """Test the creation of User attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_email_attribute(self):
        """Test the 'email' attribute of User."""
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_password_attribute(self):
        """Test the 'password' attribute of User."""
        user = User()
        user.password = "password123"
        self.assertEqual(user.password, "password123")

    def test_first_name_attribute(self):
        """Test the 'first_name' attribute of User."""
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_last_name_attribute(self):
        """Test the 'last_name' attribute of User."""
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
