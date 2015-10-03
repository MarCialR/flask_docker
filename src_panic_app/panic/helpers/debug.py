import os
import sys

def print_environ():
    for i in sorted(os.environ):
        print i, os.getenv(i)


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


def read_env_vars():
    """ If running app outside docker, --env-file has not been loaded
     we have to do it here
    :return: None
    """

    print ("The total numbers of args passed to the script: %d " %  len(sys.argv))
    if len(sys.argv) != 2:
        print ("U need to pass the environment file name")
        sys.exit(0)

    env_file_name = sys.argv[1]
    env_file = os.path.join(os.environ.get('PANIC_ROOT_DIR'), env_file_name)
    print ("Using environment file: %s " % env_file)

    with open(env_file) as _file:
        for line in _file.readlines():
            var_value = line.split("=")
            if len(var_value) == 2:
                os.environ[var_value[0].strip()] = var_value[1].strip()


def environment_checks():
    if not os.getenv('PANIC_PROJECT'):
        raise Exception('falta setear PANIC_PROJECT')

    if not os.getenv('PANIC_MODE'):
        raise Exception('falta setear PANIC_MODE: Production or Development')

