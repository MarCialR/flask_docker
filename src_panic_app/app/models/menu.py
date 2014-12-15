class MenuItem(object):
	def __init__(self, dicc):
		assert dicc.has_key('text')
		self.__dict__.update(dicc)
