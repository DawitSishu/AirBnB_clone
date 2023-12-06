#!/usr/bin/python3
"""
command enterpretor for the AIRBNB
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_help(self, arg):
        """Help command to display available commands"""
        cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
