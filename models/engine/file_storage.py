#!/usr/bin/python3
import json
import os


class FileStorage:
    """
    FileStorage class

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary that stores objects in memory.
    """

    def __init__(self):
        """
        Initializes a new FileStorage instance.
        """
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        """
        Retrieves all objects.

        Returns:
            dict: A dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object.

        Args:
            obj (object): The object to be added.
        """
        key = "{}.{}".format(obj["__class__"], obj["id"])
        self.__objects[key] = obj

    def save(self):
        """
            Saves objects to the JSON file.
        """
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        Loads objects from the JSON file.

        If the JSON file does not exist, no action is taken.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
