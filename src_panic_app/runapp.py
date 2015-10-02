import sys
def read_env_vars():
    with open("../ENVIRONMENT.env") as file:
        print file.readlines()
if __name__ == '__main__':

    import sys

    num_args = len(sys.argv)
    cmdargs = str(sys.argv)
    print ("The total numbers of args passed to the script: %d " % total)
    print ("Args list: %s " % cmdargs)
    # Pharsing args one by one
    print ("Script name: %s" % str(sys.argv[0]))
    print ("First argument: %s" % str(sys.argv[1]))
    print ("Second argument: %s" % str(sys.argv[2]))

    import os
    from panic import app, ALL_RESOURCES
    from flask.ext import restful

    api = restful.Api(app)
    app.api = api

    for res in ALL_RESOURCES:
        app.api.add_resource(res, res.url)
    if os.getenv('PANIC_RUN_APP', 'True') == 'True':
        app.run(host='0.0.0.0', port=8080, debug=True)
