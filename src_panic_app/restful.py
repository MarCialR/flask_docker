from flask import request
from flask.ext import restful
from helpers.tests import cmd_output_as_line, stdout_stderr, cmd_output_as_list

def make_api(app):
	api = restful.Api(app)

	class HelloWorld(restful.Resource):
	    def get(self):
	        return {'hello': 'worldd4'}

	api.add_resource(HelloWorld, '/json')

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

	api.add_resource(TestTestTrue, '/true')

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

	api.add_resource(TestTestFalse, '/false')        



	class TestTest(restful.Resource):
	    def get(self):
	    	output = cmd_output_as_line("gcloud compute instances list --project panic-tests")
	        return {'result': 'OK', 'info':  output.replace('\n','<br>')}

	api.add_resource(TestTest, '/info')

	class OK(restful.Resource):
	    def get(self):

	        return {'result': 'OK'}

	api.add_resource(OK, '/OK')


	class RunCommand(restful.Resource):
	    def post(self):
	    	command = request.form['lele']
	    	print "fddfd"
	    	output = cmd_output_as_list(command)
	        return {'result': 'OK', 'info': output}

	api.add_resource(RunCommand, '/runcommand')
