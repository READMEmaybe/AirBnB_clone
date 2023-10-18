#!/usr/bin/python3
"""Unittest module for the Console"""
import unittest
from unittest.mock import patch
import io
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):


    def test_create(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue()
            self.assertTrue(len(output.strip()) == 36)  # Check if an ID is printed

    def test_show(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("show BaseModel 123")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)

    def test_destroy(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy BaseModel 123")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)

    def test_all(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue()
            self.assertTrue(len(output.strip()) > 0)

    def test_count(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("count BaseModel")
            output = mock_stdout.getvalue()
            self.assertTrue(output.strip() == "0")

    def test_update(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("update BaseModel 123")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)

    def test_unknown_command(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("unknown_command")
            output = mock_stdout.getvalue()
            self.assertIn("** Unknown syntax **", output)

if __name__ == '__main__':
    unittest.main()
