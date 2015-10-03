import os
from flask import Flask
from panic.helpers.debug import read_env_vars, environment_checks

# if running app outside docker, env vars have not been loaded
if not os.getenv('PANIC_PROJECT'):
    read_env_vars()

environment_checks()


app = Flask(__name__)
app.config.from_object("configs." + os.getenv("PANIC_MODE"))


ALL_RESOURCES = []
from panic.resources_RESTFUL import resources as restful
ALL_RESOURCES.extend(restful)

from panic.tests.jsons.walker import resources as json
ALL_RESOURCES.extend(json)


import views

from blueprint_contents import contents
app.register_blueprint(contents, url_prefix='/contents')


from flask.ext import restful

api = restful.Api(app)
app.api = api

for res in ALL_RESOURCES:
    app.api.add_resource(res, res.url)
