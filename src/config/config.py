import os  # Necessary for pulling ENV VARIABLES

class Config(object):
    SECRET_KEY = os.environ.get('CRYSTAL_APP_SECRETKEY')