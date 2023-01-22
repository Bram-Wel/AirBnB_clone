#!/usr/bin/python3
"""This module contains an Command Interpreter subclass."""


import cmd
import re

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models import storage
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Entry point class for the command interpreter.

    Args:
        @cmd.Cmd : Line oriented interpreter framework class

    Attributes:
        prompt (str): String issued while soliciting input
    """

    prompt = "(hbnb) "
    _TestCompletions = ("BaseModel", "User", "State", "City", "Place"
                        "Amenity", "Review")

    def do_EOF(self, line):
        """Make a clean exit on End of file.

        Args:
            @line (str): Line buffered from input
        """
        return True

    def do_create(self, line):
        """Create a Model object.

        Args:
            @line (str): Buffered line

        Description: Prints object id after successfull creation
        and saving object to file
        """
        if (check_args(line, self)):
            obj = eval(parse_str(line)[0])()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Print string representation of class instance.

        Args:
            @line (str): Buffered line
        Description: This is done depending on object id
        """
        if (check_args(line, self)):
            key = make_key(line)
            obj = object_dict(key)
            if obj is not None:
                print(obj)

    def do_destroy(self, line):
        """Remove/delete a class instance by id.

        Args:
            @line (str): Buffered line
        """
        if (check_args(line, self)):
            key = make_key(line)
            if key:
                try:
                    del storage.all()[key]
                    storage.save()
                except KeyError:
                    print("** no instance found **")

    def do_all(self, line):
        """Print string representation of all instances.

        Args:
            @line (str): Buffered line
        Description: Can be class based or otherwise
        """
        temp = storage.all()
        try:
            class_name = parse_str(line)[0]
        except IndexError:
            print([str(i) for i in temp.values()])
        else:
            try:
                l_st = [str(i) for i in temp.values()
                        if i.__class__.__name__ == class_name]
                if l_st == []:
                    # print("Debug: ")
                    print("** class doesn't exist **")
                else:
                    print(l_st)
            except Exception as e:
                lastcmd = parse_str(self.lastcmd)[0]
                print(e, "\n help ", lastcmd)
                self.onecmd("help " + lastcmd)

    def do_update(self, line):
        """Update an instance based on class name & id.

        Args:
            @line (str): Buffered Line
        """
        args = parse_str(line)
        attr = None
        if check_args(line, self):
            key = make_key(line)
            if key:
                obj = object_dict(key)
                try:
                    attr = args[2]
                    value = args[3]
                except IndexError:
                    if attr:
                        print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    if obj:
                        setattr(obj, f"{attr}", value)
                        obj.save()

    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse_str(line)
        if check_args(line, self):
            count = 0
            for obj in storage.all().values():
                if argl[0] == obj.__class__.__name__:
                    count += 1
            print(count)

    def help_create(self):
        """Print help for do_create."""
        print("\n".join([" Create an object.", "\t[Usage]", "\t-----",
                        " create [CLASSNAME]"]))

    def help_show(self):
        """Print help for do_show."""
        print("\n".join([" Display a class instance.", "\t[Usage]",
                        "\t-------", " show [CLASSNAME] <instance id>",
                            " [CLASSNAME].show(<id>)"]))

    def help_destroy(self):
        """Print help for do_destroy."""
        print("\n".join([" Delete a class instance.", "\t[Usage]",
                        "\t-------", " destroy [CLASSNAME] <id>"]))

    def help_all(self):
        """Print help for do_all."""
        print("\n".join([" Print string representation of all instances.",
                        "\t[Usage]", "\t-------", " all", " all [CLASSNAME]",
                            " [CLASSNAME].all()"]))

    def help_update(self):
        """Print help for do_update."""
        print("\n".join([" Update class instance.", "\t[Usage]", "\t-------",
                        " update [class name] <id> <attribute name> "
                                                    + "<attribute value>"]))

    def help_quit(self):
        """Print help for do_exit."""
        print("Quit command to exit the program")

    do_quit = do_EOF

    help_EOF = help_quit

    def emptyline(self):
        """Action for an empty line entry."""
        pass

    def completedefault(self, text, line, begidx, endidx):
        """Test Completions."""
        print(HBNBCommand._TestCompletions)
        return [i for i in HBNBCommand._TestCompletions if i.startswith(text)]

    def default(self, line):
        """Defaults when command is unrecorgnised.

        Args: Line buffered from readline
        """
        args = parse_regex(line)
        if args == ():
            super().default(line)
        else:
            command = args[1]
            args_lst = [i for i in args if i is not None and i != command]
            args_str = ' '.join(args_lst)
            if command == 'all':
                self.do_all(args_str)
            elif command == 'show':
                self.do_show(args_str)
            elif command == 'destroy':
                self.do_destroy(args_str)
            elif command == 'count':
                self.do_count(args_str)
            else:
                try:
                    dct = eval(args_lst[2])
                except NameError:
                    self.do_update(args_str)
                else:
                    args_lst.pop(2)
                    args_str = ' '.join(args_lst)
                    for key, value in dct.items():
                        self.do_update(args_str + ' ' + key + ' ' + value)


def parse_str(arg):
    """Convert buffered line into arguments Tuple.

    Args:
        @arg (str): Buffered line
    Return: Tuple of arguments
    """
    return tuple(map(str, arg.split()))


def parse_regex(args):
    """Convert 0 or more nos. to integer argument tuple.

    Args:
        @args (str): Line buffered from readline
    Return: Tuple of line arguments depending on regex matches
    """
    m_str = r'(?P<class_name>\w+(?=\.))\.(?P<command>\w+(?=\())\("?(?P<id>(?<=")[\w-]*)?'
    match = re.compile(m_str)
    search_a = re.compile(r'(?P<attr_values>(?<=["\s\'])\b\w+\b(?![-\.]))')
    search_d = re.compile(r'(?P<dict_attr>(?<=\s){[\w\W]+})')

    # args = args.lower()
    res = match.match(args)
    lst = []
    if res:
        class_name = res.group('class_name')
        lst.append(class_name)
        command = res.group('command')
        lst.append(command)
        id = res.group('id')
        if id:
            lst.append(id)
            if command != 'update':
                return tuple(map(str, lst))
            res_d = search_d.search(args)
            res_list = search_a.findall(args)
            if res_d:
                dict_attr = res_d.group('dict_attr')
                lst.append(dict_attr)
            else:
                for i in res_list:
                    lst.append(i)
    return tuple(map(str, lst))


def check_args(args, obj=None):
    """Check validity of parsed class.

    Args:
        @args: Arguments tuple
        @obj: Command instance
    Description: Use obj to parse self or cmd instance for onecmd
    execution.
    Return: True if valid, False otherwise
    """
    try:
        temp = parse_str(args)[0]
    except IndexError:
        print("** class name missing **")
    else:
        try:
            temp0 = eval(temp + '()')
            key = temp + '.' + temp0.id
        except NameError:
            print("** class doesn't exist **")
        except Exception as e:
            print(e, "\n help ?")
            if obj:
                lastcmd = parse_str(obj.lastcmd)[0]
                obj.onecmd("help " + lastcmd)
        else:
            del storage.all()[key]
            return True


def make_key(args):
    """Make dictionary key from Classname & instance id.

    Args:
        @args: Line buffered by readline
    Return: A key for the instance dictionary or None on failure
    """
    name = parse_str(args)
    try:
        name[1]
    except IndexError:
        print("** instance id missing **")
        return
    return name[0] + '.' + name[1]


def object_dict(key):
    """Get object instance depending on key.

    Args:
        @key (str): A concatanation of class name & object id
    Return: A class instance or None on failure
    """
    if key:
        try:
            obj = storage.all()[key]
        except KeyError:
            print("** no instance found **")
        else:
            return obj


if __name__ == "__main__":
    HBNBCommand().cmdloop()
