import cmd
import sys
from turtle import *


class TurtleShell(cmd.Cmd):
    intro = "Welcome to the turtle shell.\nType help or ? to list commands.\n"
    prompt = "[turtle] "
    file = None

    # ---- Basic Commands -----
    def do_forward(self, arg):
        """Move the turtle by given distance: FORWARD 10"""
        forward(*parse(arg))

    def do_right(self, arg):
        """Move the turtle right by degrees: RIGHT 20"""
        right(*parse(arg))

    def do_left(self, arg):
        """Move the turtle left by degrees: LEFT 90"""
        left(*parse(arg))

    def do_goto(self, arg):
        """Move turtle to absolute position and
        change orientation: GO_TO 100 200
        """
        goto(*parse(arg))

    def do_home(self, arg):
        """Return to home position: HOME"""
        home(*parse(arg))

    def do_circle(self, arg):
        "Draw circle of given radius: CIRCLE 50"
        circle(*parse(arg))

    def do_position(self, arg):
        """Print current turtle position: POSITION"""
        print("Current position %d %d\n" % position())

    def do_heading(self, arg):
        """Print current turtle heading in degrees: HEADING"""
        print('Current heading is %d\n' % (heading(),))

    def do_color(self, arg):
        'Set the color:  COLOR BLUE'
        color(arg.lower())

    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle action(s):  UNDO'
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        reset()

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        self.close()
        bye()
        return True

    # ----- record and playback -----
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')

    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def do_EOF(self, arg):
        """Suport EOF character."""
        return True


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    TurtleShell().cmdloop()
