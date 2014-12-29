from flask import Flask
app = Flask(__name__)
app.config.from_object(__name__)

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