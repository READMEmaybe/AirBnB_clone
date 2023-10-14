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
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Retrieves all objects.

        Returns:
            dict: A dictionary of objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object.

        Args:
            obj (object): The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            Saves objects to the JSON file.
        """
        with open(FileStorage.__file_path, "w") as file:
            data = {key: value.to_dict()
                    for key, value in FileStorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """
        Loads objects from the JSON file.

        If the JSON file does not exist, no action is taken.
        """
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                loaded_data = dict(json.load(file))
                for key, value in loaded_data.items():
                    FileStorage.__objects[key] = BaseModel(**value)
