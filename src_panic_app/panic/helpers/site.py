import os


def get_static(app, filename):
    """taken from stackoverflow"""
    try:
        src = os.path.join(app.config['STATIC_DIR'], filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)



