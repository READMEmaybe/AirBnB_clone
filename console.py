#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, args):
        'Quit command to exit the program\n'
        return True

    def postcmd(self, stop, line):
        if line == 'EOF':
            return True
        return stop

    def emptyline(self):
        pass
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)
            storage.save()
    
    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** class id missing **")
        else:
            try:
                print(storage.all()[args[0]+"."+args[1]])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        # parse arg for class name and id
        # check if class name is missing
        # check if class name doesn't exist
        # check if id is missing
        # check if check if id exists
        # del __objects of said instance
        pass
    
    def do_all(self, arg):
        # check if class name exits
        # if class name is not missing: print __objects of said class
        # else: print all __objects of all classes
        pass
    
    def do_update(self, arg):
        # parse arg into: <class_name> <id> <attribute_name> <attribute_value>
        # check each token if it's missing
        # update the attribute_name with the new attribute_value
        pass
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
