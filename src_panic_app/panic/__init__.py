import os
from flask import Flask
app = Flask(__name__)
app.config.from_object(__name__)

""" import os
 os.getenv is equivalent, and can also give a default value instead of `None`
 config_to_run = os.getenv('PANIC_MODE', 'Production')
 app.config.from_envvar('CFGFILE')
 app.config.from_object('configmodule.'+config_to_run)

import os

_curdir = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    os.environ['PANIC_PROJECT'] = 'panic-tests'
    APP_TITLE = 'Panic Tests'
    TESTS_DIR = '/panic_app/panic/tests'
    DEBUG = False

class Chromebook(Config):
    APP_TITLE = 'Panic (Chromebook)'
    TESTS_DIR = '/home/marcial/repos/flask_docker/src_panic_app/panic/tests'
    DEBUG = True
"""


def print_environ():
	for i in sorted(os.environ):
		print i, os.getenv(i)

print_environ()

from helpers.tests import global_checks
global_checks()


ALL_RESOURCES = []
from panic.resources_RESTFUL import resources as resources_RESTFUL
ALL_RESOURCES.extend(resources_RESTFUL)

from panic.tests.jsons.walker import resources as resources_JSON
ALL_RESOURCES.extend(resources_JSON)


import views


from blueprint_contents import contents
app.register_blueprint(contents, url_prefix='/contents')

from pprint import pprint
print "\n\n1111111"
print "========"
pprint(app.__dict__)