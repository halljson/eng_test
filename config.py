from os.path import abspath, join, dirname
basedir = abspath(dirname(__file__))
STATIC_FOLDER = join(*[basedir, "application", "static"])

# from os import environ
# FLASK_DEBUG = environ.get('FLASK_DEBUG', False)
FLASK_DEBUG = True