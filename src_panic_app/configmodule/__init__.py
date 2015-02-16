import os

class Config(object):
    os.environ['PANIC_PROJECT'] = 'panic-tests'
    APP_TITLE = 'Panic Tests'
    TESTS_DIR = '/root/panic_app/panic/tests'
    DEBUG = False

class Production(Config):
	pass

class Dev(Config):
    DEBUG = True

class Chromebook(Config):
    APP_TITLE = 'Panic (Chromebook)'
    TESTS_DIR = '/home/marcial/repos/flask_docker/src_panic_app/panic/tests'
    DEBUG = True

   