from helpers.html import to_br

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
			
	def extend_items(self):
		extended_items = [  MenuItem({'text':'Json Tests',
								'url':'tests/json_tests'}),
							MenuItem({'text':'Nose Tests',
								'url':'tests/nose_tests'}),
							MenuItem({'text':'Shell Tests',
								'url':'tests/shell_tests'}) ]
		self.set_items(self.items + extended_items)


menu = Menu([ MenuItem({'text':'App Engine',
			'url':'tests/appengine'}),
		MenuItem({'text':'Compute Engine',
			'url':'tests/computeengine'}),
		MenuItem({'text':'Debug',
			'url':'debug'}) ])

menu.extend_items()


