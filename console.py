#!/usr/bin/python3
"""This module contains an Command Interpreter subclass."""


import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point class for the command interpreter.

    Args:
        @cmd.Cmd : Line oriented interpreter framework class
        
    Attributes:
        prompt (str): String issued while soliciting input
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Make a clean exit on End of file.

        Args:
            @line (str): Line buffered from input
        """
        return True

    def help_quit(self):
        """Print help for do_exit.

        Args:
            @line (str): Command string read from input
        """
        print("Quit command to exit the program")

    do_quit = do_EOF
    help_EOF = help_quit

    def emptyline(self):
        """Action for an empty line entry."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
