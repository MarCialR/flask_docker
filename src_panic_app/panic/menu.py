import os
from helpers.site import TESTS_DIR, NOSE_TESTS_DIR
from helpers.html import to_br
from panic import ALL_RESOURCES as resources

class Walker(object):

	def walk(self):
		info = ""
		info += "This is using getsize to see how much every file consumes\n"
		info += "---------------\n"
		from os.path import join, getsize
		zero = len(TESTS_DIR)
		for root, dirs, files in os.walk(TESTS_DIR):
		    info += "\n" + root[zero:]
		    info += " consumes " + str(sum([getsize(join(root, name)) for name in files]))
		    info += " bytes in " + str(len(files)) +  " files"

		return to_br(info)
	
	def search_for_json(self):
		return MenuItem({'text':'Json Tests',
			'url':'tests/json_tests'})

	def _collect_tests_from_dir(self, dir_to_collect):
		#from pprint import pprint
		#APP_ENGINE_TESTS_DIR = "/home/marcial/repos/flask_docker/src_panic_app/panic/tests/noses/test_appengine"
		from nose.config import Config
		conf = Config()
		from nose.loader import TestLoader
		loader = TestLoader()
		from nose.plugins.collect import CollectOnly, TestSuiteFactory, TestSuite
		collect = CollectOnly()
		collect.conf = conf
		collect.prepareTestLoader(loader)

		tests = loader.loadTestsFromDir(dir_to_collect)

		suite = TestSuite()
		suite.addTests(tests)
		#from nose.core import TextTestRunner
		#TextTestRunner().run(suite
		return suite

	def search_for_noses(self):
		
		print "NOSE_TESTS_DIR: %s" %NOSE_TESTS_DIR

		tests = self._collect_tests_from_dir(NOSE_TESTS_DIR)._tests

		return MenuItem({'text':'Nose Tests',
			'url':'tests/nose_tests'})
	
	def search_for_shell(self):
		return MenuItem({'text':'Shell Tests',
			'url':'tests/shell_tests'})

class MenuItem(object):
	def __init__(self, dicc):
		self.__dict__.update(dicc)
		self._isok()
	
	def _isok(self):
		""" does the sanity checks"""
		assert self.__dict__.has_key('text')
		assert self.__dict__.has_key('url')


class Menu(object):
	
	def __init__(self, items):
		self.items = items
		self.walker = Walker()
		self.jsons = []
		self.noses = []
		self.shells = []
		self.search()


	def set_items(self, items=None):
		if items and len(items)>0:
			self.items = items		

	def get_html(self):
		html = ""
		for item in self.items:
			html += """
                        <li>
                            <a href="javascript:load_contents('%s')"><i class="fa fa-cloud fa-fw"></i> %s</a>
                        </li>
""" % (item.url, item.text)

		return html

	def get_text_by_url(self, url):
		for i in self.items:
			if i.url == url:
				return i.text
		return 'Menu Item not found for url: ' + url



	def search(self):
		self.jsons.append(self.walker.search_for_json())
		self.noses.append(self.walker.search_for_noses())
		self.shells.append(self.walker.search_for_shell())
			
	def extend_items(self):
		extended_items = [  MenuItem({'text':'Json Tests',
								'url':'tests/json_tests'}),
							MenuItem({'text':'Nose Tests',
								'url':'tests/nose_tests'}),
							MenuItem({'text':'Shell Tests',
								'url':'tests/shell_tests'}) ]
		self.set_items(self.items + extended_items)



	def get_tests_for_page(self, page):
	    tests = []
	    for res in resources:
	        if res.menu == page or page=='tests':
	            tests.append({'id': res.name, 'url': res.url, 'name': res.name})    
	    return tests

menu = Menu([ MenuItem({'text':'App Engine',
			'url':'tests/appengine'}),
		MenuItem({'text':'Compute Engine',
			'url':'tests/computeengine'}),
		MenuItem({'text':'Debugging tools',
			'url':'debug'}) ])

menu.extend_items()


