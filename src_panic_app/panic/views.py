import os
from flask import Response, render_template

from panic import app
from menu import menu
from helpers.site import get_static, STATIC_DIR


@app.route('/', methods=['GET'])
def index():
    return render_template( 'index.html', menu = menu)

@app.route('/<page>.html', methods=['GET'])
def old_html(page='index'):
    return render_template( 'sbtadmin/'+page+'.html', menu = menu)    

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

