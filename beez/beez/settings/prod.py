import os
from socket import gethostname, gethostbyname

from beez.settings.base import *

ALLOWED_HOSTS = os.getenv('BEEZ_ALLOWED_HOSTS', '').split(',')

# We add these hosts to allow Dokku's CHECKS feature to work
ALLOWED_HOSTS.append(gethostname())
ALLOWED_HOSTS.append(gethostbyname(gethostname()))