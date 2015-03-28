import os

_thisfiledir = os.path.abspath(os.path.dirname(__file__))

def get_dir_in_app(_dir):  # pragma: no cover
    """returns the absolute path of the main app folders"""
    return os.path.normpath(os.path.join(os.path.join(_thisfiledir, '..' ), _dir))


STATIC_DIR = get_dir_in_app("static")
TEMPLATES_DIR = get_dir_in_app("templates")
TESTS_DIR = get_dir_in_app("tests")
NOSE_TESTS_DIR = get_dir_in_app("tests/noses")

del _thisfiledir

def get_static(filename):
    """taken from stackoverflow"""
    try:
        src = os.path.join(STATIC_DIR, filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

def app_info(app):
    from pprint import pprint
    print "\n\nAPP DICT"
    print "========"
    pprint(app.__dict__)    
    print "\n\nAPI.resources"
    print "==========="
    pprint(app.api.resources)

    print "\n\nAPI"
    print "==="
    pprint(app.api.__dict__)

