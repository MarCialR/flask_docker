
from flask import Flask
from helpers.site import debug_info
from flask.ext import restful
from restfull.restful2 import resources
from views import make_routes

app = Flask(__name__)
app.config.from_object(__name__)

api = restful.Api(app)

for res in resources:
    api.add_resource(res, res.url)

#debug_info(app, api)



make_routes(app, resources)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

    """from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8080)
    IOLoop.instance().start()"""