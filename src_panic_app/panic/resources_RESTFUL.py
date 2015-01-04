from flask import request
from helpers.tests import cmd_output_as_line, stdout_stderr, cmd_output_as_lines
from flask.ext.restful import Resource

resources = []


"""
SESTE

/repos/flask_docker/src_panic_app/app/tests/python/nosetests/test_appengine
"""

class OK(Resource):
    url = '/ok'
    tipe = 'ok'
    name = 'OK'
    menu = 'appengine'
    def get(self):
        import os
        os.chdir('/root/panic_app/panic/tests/noses/test_appengine/')
        output = cmd_output_as_lines("nosetests")
        return {'result': 'OK', 'info':"</br>".join(output)}        


resources.append(OK)

class Trivial(Resource):
    url = '/Trivial'
    tipe = 'Trivial'
    name = 'Trivial'
    menu = 'appengine'
    def get(self):
        import os
        os.chdir('/root/panic_app/panic/tests/noses/trivial_tests')
        output = cmd_output_as_lines("nosetests")
        return {'result': 'OK', 'info':"</br>".join(output)}        


resources.append(Trivial)

class RunCommand(Resource):
    url = '/runcommand'
    tipe = 'free'
    name = 'RunCommand'
    menu = 'appengine'
    def post(self):
    	command = request.form['command']
        output = cmd_output_as_line(command)
        return {'result': 'OK', 'info': output}

resources.append(RunCommand)
