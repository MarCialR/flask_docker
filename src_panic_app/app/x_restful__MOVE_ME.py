from flask import request
from helpers.tests import cmd_output_as_line, stdout_stderr, cmd_output_as_lines
from flask.ext.restful import Resource

resources = []


"""
SESTE

/repos/flask_docker/src_panic_app/app/tests/python/nosetests/test_appengine
"""
import os
class OK(Resource):
    url = '/ok'
    tipe = 'ok'
    name = 'OK'
    menu = 'appengine'
    def get(self):
        os.chdir('/root/panic_app/app/tests/noses/test_appengine/')
        output = cmd_output_as_lines("nosetests")
        return {'result': 'OK', 'info':"</br>".join(output)}        


resources.append(OK)


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


"""
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', 
'__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_blueprint_setup_add_url_rule_patch', 
'_complete_url', '_deferred_blueprint_init', '_has_fr_route', '_init_app', '_register_view', 
'_should_use_fr_error_handler', 'add_resource', 'app', 'blueprint', 'blueprint_setup', 'catch_all_404s',
'decorators', 'default_mediatype', 'endpoints', 'error_router', 'errors', 'handle_error', 'init_app',
'make_response', 'mediatypes', 'mediatypes_method', 'output', 'owns_endpoint', 'prefix', 'representation',
'representations', 'resource', 'resources', 'unauthorized', 'url_for', 'url_part_order', 'urls']
"""
