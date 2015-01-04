import os
from flask import Response, render_template, jsonify

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



from flask import  jsonify
from helpers.tests import cmd_output_as_lines
from collection import collection
import os

@app.route('/noses/<what>', methods=['GET'])
def test_nose(what):
    """
    from nose.core import TextTestRunner
    from nose.plugins.collect import TestSuite    
    
    test = collection.noses.get_test(what)
    suite = TestSuite()
    suite.addTest(test)
    

    import sys
    import unittest
    import logging

    logger = logging.getLogger()
    logger.level = logging.DEBUG
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)

    stream_handler.stream = sys.stdout
    
    TextTestRunner().run(suite)
    logger.removeHandler(stream_handler)    
    
    return jsonify( result='OK')"""
    
    print (what +"\n")* 5

    os.chdir('/root/panic_app/panic/tests/noses')
    output = cmd_output_as_lines("nosetests %s" % what)
    last_line = str(output[-1:]) # ['OK\r\n']
    result = 'OK' if (last_line[2:4] == 'OK') else 'KO'
    return jsonify(result= result, info="</br>".join(output))

@app.route('/noses_direct/<what>', methods=['GET'])
def test_noses_direct(what):
    print (what +"\n---")* 20
    test = collection.get_nose_test(what)

    from nose.plugins.collect import TestSuite

    suite = TestSuite()
    suite.addTest(test)

    from nose.core import TextTestRunner
    TextTestRunner().run(suite)
    logger.removeHandler(stream_handler)    
    
    return jsonify( result='OK')