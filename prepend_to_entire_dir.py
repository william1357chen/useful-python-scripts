import os
from os import listdir
from copy import copy
# This script adds whatever you want to all files in
# the current working directory without overwritting.
# any files. The added data will be on line 1
# The files can be python scripts, text file, etc.


def add_line_to_every_file(cmd, file_extension):
    for instance in listdir(os.getcwd()):
        if os.path.isfile(instance):

            instance_ex = copy(instance).split('.')[-1]
            if instance_ex == file_extension:
                line_prependerv2(cmd, instance)


def line_prependerv2(cmd, filename):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(cmd.strip('\r\n') + '\n' + content)
