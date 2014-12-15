import os
from flask import Flask, Response, render_template
from helpers.site import get_static, STATIC_DIR

from menu import menu, get_menu_text_by_url
from jinja2 import TemplateNotFound
from helpers.tests import get_tests_for_page

def make_routes(app, resources):


    @app.route('/index.html', methods=['GET'])
    def index():
        return render_template( 'index.html',
                           menu = menu)
                           
    @app.route('/', methods=['GET'])
    @app.route('/tests/<page>', methods=['GET'])
    def tests(page='appengine'):
        return render_template( 'tests.html',
                           title = get_menu_text_by_url('tests/' + page),
                           tests = get_tests_for_page(resources, page),
                           menu = menu)

    @app.route('/<page>.html', methods=['GET'])
    def old_html(page='index'):
        content = get_static(page+'.html')
        return Response(content, mimetype="text/html")

    #@app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def get_resource(path):
        mimetypes = {
            ".css": "text/css",
            #".html": "text/html",
            ".js": "application/javascript",
        }
        complete_path = os.path.join(STATIC_DIR, path)
        ext = os.path.splitext(path)[1]
        mimetype = mimetypes.get(ext, "text/html")
        content = get_static(complete_path)
        return Response(content, mimetype=mimetype)

