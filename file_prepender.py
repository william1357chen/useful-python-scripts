import subprocess

# This script adds whatever you want to an existing file
# without overwritting. The added data will be on line 1
# The file can be python scripts, text file, etc.


def line_prependerv1(cmd, filename):
    result = subprocess.run(
        ['cat', filename], stdout=subprocess.PIPE, text=True, check=True)
    file_output = result.stdout
    file_output = cmd + '\n' + file_output

    with open(filename, 'w') as f:
        f.write(file_output)


def line_prependerv2(cmd, filename):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(cmd.strip('\r\n') + '\n' + content)
