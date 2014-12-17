from panic import app, ALL_RESOURCES

from flask.ext import restful
api = restful.Api(app)
app.api = api

for res in ALL_RESOURCES:
    app.api.add_resource(res, res.url)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

