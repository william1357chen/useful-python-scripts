import os
from os import listdir
import subprocess
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
                add_line_to_file(cmd, instance)


def add_line_to_file(cmd, filename):
    result = subprocess.run(
        ['cat', filename], stdout=subprocess.PIPE, text=True, check=True)
    file_output = result.stdout
    file_output = cmd + '\n' + file_output

    with open(filename, 'w') as f:
        f.write(file_output)
