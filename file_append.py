import subprocess

# This script adds whatever you want to an existing file
# without overwritting. The added data will be on line 1
# The file can be python scripts, text file, etc.


def add_line_to_file(cmd, filename):
    result = subprocess.run(
        ['cat', filename], stdout=subprocess.PIPE, text=True, check=True)
    file_output = result.stdout
    file_output = cmd + '\n' + file_output

    with open(filename, 'w') as f:
        f.write(file_output)
