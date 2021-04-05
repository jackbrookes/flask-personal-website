import os
DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))
BLOGGING_URL_PREFIX = "/posts"
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
FREEZER_DESTINATION = 'jackbrookes.github.io'
FREEZER_DESTINATION_IGNORE = ['.git*', 'CNAME']
