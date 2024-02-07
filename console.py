import cmd


class HBNBCommand(cmd.Cmd):
    """AirBNB commandline utility."""
    prompt = '(hbnb) '

    def do_Quit(self, person):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """closes the terminal"""
        return True

    def emptyline(self):
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
