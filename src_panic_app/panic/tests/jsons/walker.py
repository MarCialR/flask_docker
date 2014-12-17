from panic.helpers.tests import stdout_stderr  # REMOVE THIS IMPORT
from flask.ext.restful import Resource
from tests import json_tests
from pprint import pprint

resources = []

def get(self):
    from random import randint
    from time import sleep

    #sleep(randint(1,4))    
    stdout, stderr = stdout_stderr(self.command)
    return {'result': 'OK' if stdout == self.expected else 'KO',
            'info': stdout.replace('\n','<br>')}

def build_testclass(test_dict):
    test_dict.update({'get':get})
    test_dict.update({'url':"/"+test['name']})
    return type(str(test_dict['name']), (Resource,), test_dict)

for test in json_tests:
    print "*"*10, "\n", pprint(test)
    resources.append(build_testclass(test))