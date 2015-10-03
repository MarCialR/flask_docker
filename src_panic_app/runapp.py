import os
os.environ['PANIC_ROOT_DIR'] = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    from panic import app

    if os.getenv('PANIC_RUN_APP', 'True') == 'True':
        app.run(host='0.0.0.0', port=8080, debug=True)
