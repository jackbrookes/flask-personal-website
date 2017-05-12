import private_config
import os
DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = private_config.KEY
BLOGGING_URL_PREFIX = "/posts"
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
