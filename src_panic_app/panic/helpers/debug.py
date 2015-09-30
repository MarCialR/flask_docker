import os

def print_environ():
	for i in os.environ:
		print i, os.getenv(i)
