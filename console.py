#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        'Quit command to exit the program'
        return True

    def do_EOF(self, args):
        'Quit command to exit the program'
        return True

    def postcmd(self, stop, line):
        if line == 'EOF':
            return True
        return stop

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
