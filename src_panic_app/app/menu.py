class MenuItem(object):
	def __init__(self, dicc):
		assert dicc.has_key('text')
		self.__dict__.update(dicc)



class Menu(object):
	def __init__(self, items):
		self.items = items

	def populate(self):
		html = ""
		for item in self.items:
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


menu = Menu([ MenuItem({'text':'App Engine',
			'url':'tests/appengine'}),
		MenuItem({'text':'Compute Engine',
			'url':'tests/computeengine'}),
		MenuItem({'text':'Debugging tools',
			'url':'debug'}) ])



