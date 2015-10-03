__author__ = 'mroman'

import os

thisfiledir = os.path.abspath(os.path.dirname(__file__))
appdir = os.path.normpath(os.path.join(thisfiledir, '../panic' ))


class Config(object):
    APP_TITLE = os.environ['PANIC_PROJECT']
    STATIC_DIR = os.path.join(appdir, 'static')
    TEMPLATES_DIR = os.path.join(appdir, 'templates')
    TESTS_DIR = os.path.join(appdir, 'tests')
    NOSE_TESTS_DIR = os.path.join(appdir, 'tests/noses')
    DEBUG = False


class Production(Config):
    pass


class Development(Config):
    APP_TITLE = Config.APP_TITLE + '(Dev)'
    DEBUG = True

del thisfiledir
