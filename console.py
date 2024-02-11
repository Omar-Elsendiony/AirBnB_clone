#!/usr/bin/python3
"""
console module starts a console that takes user inputs by
providing a prompt that waits for the input
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """AirBNB commandline utility."""
    prompt = '(hbnb) ' #prompt 

    def do_create(self, line):
        """creates a new instance of the class with the provided name"""
        parsed_line = parse(line)
        try:
            if (len(parsed_line) == 0):
                print("** class name missing **")
            else:
                className = parsed_line[0]
                if (className == ""): 
                    print("** class name missing **")
                else:
                    instance = globals()[className]()
                    if (className == "BaseModel"):
                        print(instance.id)
                        instance.save()
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """destroys the instance of the class given the id and classname"""
        parsed_line = parse(line)
        try:
            if (len(parsed_line) == 0):
                print("** class name missing **")
            elif (len(parsed_line) < 2):
                instance = globals()[(parsed_line[0])]()
                print("** instance id missing **")
            else:
                className = parsed_line[0]
                id = (parsed_line[1])
                fs = FileStorage()
                fs.reload()
                all_reloaded = fs.all()
                obj_reloaded = all_reloaded.get("{}.{}".format(className, id))
                if (obj_reloaded is None):
                    print("** no instance found **")
                else:
                    del all_reloaded[className + "." + id]
                    fs.save()
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """creates a new instance of the class with the provided name"""
        parsed_line = parse(line)
        try:
            if (len(parsed_line) == 0):
                print("** class name missing **")
            elif (len(parsed_line) < 2):
                instance = globals()[parsed_line[0]]()
                print("** instance id missing **")
            else:
                className = parsed_line[0]
                id = parsed_line[1]
                fs = FileStorage()
                fs.reload()
                all_reloaded = fs.all()
                # instance = globals()[parsed_line[0]]()
                obj_reloaded = all_reloaded.\
                    get("{}.{}".format(className, id))
                if (obj_reloaded is None):
                    print("** no instance found **")
                else:
                    print(obj_reloaded)
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, line):
        """creates a new instance of the class with the provided name"""
        parsed_line = parse(line)
        try:
            if (len(parsed_line) == 0):
                print("** class name missing **")
            else:
                className = parsed_line[0]
                fs = FileStorage()
                fs.reload()
                all_reloaded = fs.all()
                allinstances = []
                for k, v in all_reloaded.items():
                    classNameExtracted = k.split(".")[0]
                    if (className == classNameExtracted):
                        allinstances.append(v.__str__())
                print(allinstances)
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """updates the instance attribute with certain value"""
        parsed_line = parse(line)
        try:
            if (len(parsed_line) == 0):
                print("** class name missing **")
            elif (len(parsed_line) < 2):
                instance = globals()[parsed_line[0]]()
                print("** instance id missing **")
            else:
                className = parsed_line[0]
                id = parsed_line[1]
                fs = FileStorage()
                fs.reload()
                all_reloaded = fs.all()
                obj_reloaded = all_reloaded.get("{}.{}".format(className, id))
                if (obj_reloaded is None):
                    print("** no instance found **")
                else:
                    if (len(parsed_line) < 3):
                        print("** attribute name missing **")
                    else:
                        attr = parsed_line[2]
                        if (len(parsed_line) < 4):
                            print("** value missing **")
                        else:
                            # setattr(obj_reloaded, attr, parsed_line[3])
                            obj_reloaded.__dict__[attr] = \
                                eval(parsed_line[3])
                            print(obj_reloaded)
                            fs.save()
        except KeyError:
            print("** class doesn't exist **")

    def do_Quit(self, person):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """closes the terminal"""
        return True

    def emptyline(self):
        "Enter does nothing"
        return


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(str, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
