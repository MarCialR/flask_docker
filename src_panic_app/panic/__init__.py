from flask import Flask
app = Flask(__name__)
app.config.from_object(__name__)

ALL_RESOURCES = []
from panic.resources_RESTFUL import resources as resources_RESTFUL
ALL_RESOURCES.extend(resources_RESTFUL)

from panic.tests.jsons.walker import resources as resources_JSON
ALL_RESOURCES.extend(resources_JSON)


import views
