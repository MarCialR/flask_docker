from models.menu import MenuItem as MI

menu = [ MI({'text':'App Engine',
			'url':'tests/appengine'}),
		MI({'text':'Compute Engine',
			'url':'tests/computeengine'}) ]

def get_menu_text_by_url(url):
	for i in menu:
		if i.url == url:
			return i.text
	return 'Menu Item not found for url: ' + url
