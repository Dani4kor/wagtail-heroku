from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass
