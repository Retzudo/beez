from beez.settings.base import *

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = os.getenv('BEEZ_SECRET_KEY', 'secret')