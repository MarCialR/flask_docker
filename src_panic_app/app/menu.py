import os
from helpers.site import TESTS_DIR
from helpers.html import to_br

class Walker(object):

	def walk(self):
		info = ""
		info += "This is using getsize to see how much every file consumes\n"
		info += "---------------\n"
		from os.path import join, getsize
		for root, dirs, files in os.walk(TESTS_DIR):
		    info += root + " consumes "
		    info += str(sum([getsize(join(root, name)) for name in files]))
		    info += " bytes in " + str(len(files)) +  " non-directory files"

		for root, dirs, files in os.walk(TESTS_DIR):
		    info += root + " consumes "
		    info += str(sum([getsize(join(root, name)) for name in files]))
		    info += " bytes in " + str(len(files)) +  " non-directory files"

		return to_br(info)

class MenuItem(object):
	def __init__(self, dicc):
		self.__dict__.update(dicc)
		self._isok()
	
	def _isok(self):
		""" does the sanity checks"""
		assert self.__dict__.has_key('text')
		assert self.__dict__.has_key('url')



class Menu(object):
	walker = Walker()
	
	def __init__(self, items):
		self.items = items

	def populate(self, items = None):
		html = ""
		if not items:
			items = self.items
		for item in items:
			html += """
                        <li>
                            <a href="/%s"><i class="fa fa-table fa-fw"></i> %s</a>
                        </li>
""" % (item.url, item.text)
		return html

	def get_text_by_url(self, url):
		for i in self.items:
			if i.url == url:
				return i.text
		return 'Menu Item not found for url: ' + url



class Menu2(Menu):
	
	jsons = []
	noses = []
	shells = []

	def __init__(self, items):
		super(Menu2, self).__init__(items)
		self.search()

	def search(self):
		self.search_for_json()
		self.search_for_noses()
		self.search_for_shell()
			
	
	def search_for_json(self):
		self.jsons.append(MenuItem({'text':'Json Tests',
			'url':'tests/json_tests'}))
	
	def search_for_noses(self):
		self.noses.append(MenuItem({'text':'Nose Tests',
			'url':'tests/nose_tests'}))
	
	def search_for_shell(self):
		self.shells.append(MenuItem({'text':'Shell Tests',
			'url':'tests/shell_tests'}))
	
	def items_extended(self):
		return self.jsons + self.noses + self.shells + self.items
		
	def populate(self):
		return super(Menu2, self).populate(self.items_extended())
		


menu = Menu2([ MenuItem({'text':'App Engine',
			'url':'tests/appengine'}),
		MenuItem({'text':'Compute Engine',
			'url':'tests/computeengine'}),
		MenuItem({'text':'Debugging tools',
			'url':'debug'}) ])


