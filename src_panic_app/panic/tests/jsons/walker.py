from panic.helpers.tests import cmd_output_as_line, cmd_output_as_lines  # REMOVE THIS IMPORT
from flask.ext.restful import Resource
from tests import json_tests
from pprint import pprint

resources = []


def get(self):

    """stdout, stderr = stdout_stderr(self.command)
    print "stdout\n", stdout
    print "stderr\n", stderr 
    if stdout == self.expected:
        return {'result': 'OK' ,
            'info': stdout.replace('\n','<br>')}
    else:
        return {'result': 'KO' ,
            'info': stderr.replace('\n','<br>')}"""

    """output = cmd_output_as_line(self.command)
    if output == self.expected:
        return {'result': 'OK' ,
            'info': output.replace('\r\n','<br>').replace('\n','<br>')}
    else:
        return {'result': 'KO' ,
            'info': output.replace('\r\n','<br>').replace('\n','<br>')}"""

    output = [l.replace('\r\n','<br>').replace('\n','<br>') for l in cmd_output_as_lines(self.command)]
    return {'result': 'OK' ,
            'info': "".join(output)}


def build_testclass(test_dict):
    test_dict.update({'get':get})
    test_dict.update({'url':"/"+test['name']})
    return type(str(test_dict['name']), (Resource,), test_dict)

for test in json_tests:
    print "*"*10, "\n", pprint(test)
    resources.append(build_testclass(test))