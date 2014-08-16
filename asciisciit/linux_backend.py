"""

linux_backend.py

Linux support functions.

"""

import os


def clear_term():
    print(chr(27) + "[2J")


def set_terminal_size(size):
    """
    Can't get this to work....
    """
    rows, cols = size
    #os.system("stty rows %s" % rows)
    #os.system("stty cols %s" % cols)
    return


def new_term(command, size=None):
    """
    Open a new terminal with specified geometry and a command to run.
    """
    if size:
        width, height = size
        os.system("gnome-terminal --geometry %sx%s -e 'bash -c \"python %s\"'" %
                  (width+1, height+3, command))
    else:
        os.system("gnome-terminal -e 'bash -c \"python %s\"'" % (command))


if __name__ == '__main__':
    pass