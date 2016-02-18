__author__ = 'Sourabh Dev'

from .project import *


if __name__ == '__main__':
    app.secret_key = 'this_key_is_secret'
    app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
    app.debug = True
    app.jinja_env.globals['csrf_token'] = generate_csrf_token
    app.run(host='0.0.0.0')
