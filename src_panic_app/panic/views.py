import os
from flask import Flask, Response, render_template
from helpers.site import get_static, STATIC_DIR

from menu import menu
from jinja2 import TemplateNotFound
from helpers.tests import get_tests_for_page
from panic import app
from pprint import pprint
print "\n\n1111111"
print "========"
pprint(app.__dict__)



@app.route('/gcloud.html')
def get_gcloud_example():
    complete_path = os.path.join(STATIC_DIR, 'gcloud.html')
    content = get_static(complete_path)
    return Response(content, mimetype="text/html")






from panic import ALL_RESOURCES as resources
@app.route('/index.html', methods=['GET'])
def index():
    return render_template( 'index.html',
                       menu = menu)
                       
@app.route('/', methods=['GET'])
@app.route('/tests/<page>', methods=['GET'])
def tests(page='appengine'):
    return render_template( 'tests.html',
                       title = menu.get_text_by_url('tests/' + page),
                       tests = get_tests_for_page(resources, page),
                       menu = menu)


@app.route('/debug', methods=['GET'])
def debug():
    return render_template( 'debug.html',
                            title = 'Debugging tools',
                            menu = menu)

@app.route('/<page>.html', methods=['GET'])
def old_html(page='index'):
    return render_template( 'sbtadmin/'+page+'.html',
                       title = menu.get_text_by_url('tests/' + page),
                       tests = get_tests_for_page(resources, page),
                       menu = menu)        
    """content = get_static(page+'.html')
    return Response(content, mimetype="text/html")"""

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

