from flask import request
from test_helpers import cmd_output_as_line, stdout_stderr
from flask.ext import restful



class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'worldd4'}



class TestTestTrue(restful.Resource):
    def get(self):
        expected_output="""NAME                   NETWORK SRC_RANGES    RULES                        SRC_TAGS TARGET_TAGS
default-allow-http     default 0.0.0.0/0     tcp:80                                http-server
default-allow-icmp     default 0.0.0.0/0     icmp
default-allow-internal default 10.240.0.0/16 tcp:1-65535,udp:1-65535,icmp
default-allow-rdp      default 0.0.0.0/0     tcp:3389
default-allow-ssh      default 0.0.0.0/0     tcp:22
"""
        stdout, stderr = stdout_stderr("gcloud compute firewall-rules list --project panic-tests")
        if stdout == expected_output:
        	return {'result': 'OK', 'info': stdout.replace('\n','<br>')}
        else:
        	return {'result': 'KO', 'info': stdout.replace('\n','<br>')}

class TestTestFalse(restful.Resource):
    def get(self):
        expected_output="""NAME                   NETWORK SRC_RANGES    RULES                        SRC_TAGS TARGET_TAGS
default-allow-icmp     default 0.0.0.0/0     icmp
default-allow-internal default 10.240.0.0/16 tcp:1-65535,udp:1-65535,icmp
default-allow-rdp      default 0.0.0.0/0     tcp:3389
default-allow-ssh      default 0.0.0.0/0     tcp:22
"""
        stdout, stderr = stdout_stderr("gcloud compute firewall-rules list --project panic-tests")
        if stdout == expected_output:
        	return {'result': 'OK', 'info': stdout.replace('\n','<br>')}
        else:
        	return {'result': 'KO', 'info': stdout.replace('\n','<br>')}



class TestTest(restful.Resource):
    def get(self):
    	output = cmd_output_as_lines("gcloud compute instances list --project panic-tests")
        return {'result': 'OK', 'info':  output.replace('\n','<br>')}

class OK(restful.Resource):
    def get(self):

        return {'result': 'OK'}


class RunCommand(restful.Resource):
    def post(self):
    	command = request.form['lele']
    	print "fddfd"
    	output = cmd_output_as_line(command)
        return {'result': 'OK', 'info': output}

resources = [(HelloWorld, '/json'),
        (TestTestTrue, '/true'),
        (TestTestFalse, '/false'),
        (TestTest, '/info'),
        (OK, '/OK'),
        (RunCommand, '/runcommand')]

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
