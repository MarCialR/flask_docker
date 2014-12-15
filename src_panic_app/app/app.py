import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)


from flask.ext import restful
api = restful.Api(app)

from restfull.restful2 import resources
for res in resources:
    api.add_resource(res, res.url)

debug = True

if debug:

    from pprint import pprint
    print "\n\nAPI.resources"
    print "==========="
    pprint(api.resources)

    print "\n\nAPI"
    print "==="
    pprint(api)

    print "\n\nAPP"
    print "==="

    pprint(app)

    app.api = api
    print "\n\nAPP DICT"
    print "========"
    pprint(app.__dict__)

from menu import menu
from views import make_routes
make_routes(app, resources)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

    """from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8080)
    IOLoop.instance().start()"""