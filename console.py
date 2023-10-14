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
        """ """
        if not arg:
            print("** class name missing **")
            return
        elif arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new = BaseModel()
        print(new.id)
        storage.save()
    
    def do_show(self, arg):
        # parse arg for class name and id
        # check if class name is missing
        # check if class name doesn't exist
        # check if id is missing
        # check if check if id exists
        # print __objects of said instance
        pass

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
