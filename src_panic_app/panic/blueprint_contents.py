from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound
from menu import menu



contents = Blueprint('contents', __name__,
                        template_folder='templates')

@contents.route('/tests/<what>', methods=['GET'])
def test_suite(what):
    try:
        return jsonify(	result='OK',
        				contents=render_template('contents/tests.html',
        				title = menu.get_text_by_url('tests/' + what),
                       	tests = menu.get_tests_for_page(what))
        			   )
    except TemplateNotFound:
        return jsonify(result='KO')

@contents.route('/debug', methods=['GET'])
def debug():
    try:
        return jsonify(	result='OK',
        				contents=render_template('contents/debug.html',
                        title = 'Debugging tools',
                        menu= menu)
        			   )
    except TemplateNotFound:
        return jsonify(result='KO')	

