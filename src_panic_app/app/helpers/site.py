import os

def get_dir(_dir):  # pragma: no cover
    return os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..' ), _dir)

STATIC_DIR = get_dir("static")

def get_static(filename):
    """taken from stackoverflow"""
    try:
        src = os.path.join(STATIC_DIR, filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

def debug_info(app, api):
    from pprint import pprint
    print "\n\nAPI.resources"
    print "==========="
    pprint(api.resources)

    print "\n\nAPI"
    print "==="
    pprint(api)

    print "\n\nAPP"
    print "==="

    pprint(app)

    app.api = api
    print "\n\nAPP DICT"
    print "========"
    pprint(app.__dict__)	