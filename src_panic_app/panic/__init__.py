from flask import Flask
app = Flask(__name__)
app.config.from_object(__name__)



import os
# os.getenv is equivalent, and can also give a default value instead of `None`
config_to_run = os.getenv('PANIC_MODE', 'Production')
#app.config.from_envvar('CFGFILE')
app.config.from_object('configmodule.'+config_to_run)



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