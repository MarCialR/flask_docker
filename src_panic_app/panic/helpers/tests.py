import re
import subprocess
from pexpect import spawn, ExceptionPexpect

foo_output = ".... OK"

def stdout_stderr(command):
    """
    opens subprocess and returns stdout, stderr for given command
    """
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return p.communicate()


def cmd_output_as_lines(command):
    """
    pexpects command and returns output as a lines list
    """
    output = []
    try:
        child = spawn(command, timeout=None)                              
        for line in child:                                                  
            output.append(line)
    except ExceptionPexpect:
        output.append("Command '%s' could not be executed properly!" %command)
    return output


def cmd_output_as_line(command):
    """
    pexpects command and returns output lines joined in a string
    """
    try:
        output = "".join(spawn(command, timeout=None))
    except ExceptionPexpect as e:
        output = str(e)
    return output



def write_to_logg(what_to_log):

    logg_file = "/home/mroman/repos/notebooks/notebooks/google/1_Panic_tests/tests/logg"
    with open(logg_file,"a") as file:
        file.write(what_to_log)

"""
def _unidiff_output(expected, actual):
    ""
    Helper function. Returns a string containing the unified diff of two multiline strings.
    ""

    import difflib
    expected=expected.splitlines(1)
    actual=actual.splitlines(1)

    diff=difflib.unified_diff(expected, actual)

    return ''.join(diff)
"""


