"""
WSGI config for LPGallery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LPGallery.settings')

application = get_wsgi_application()

# application = MyWSGIApp()
# application = WhiteNoise(application, root='/gallery/static')
# application.add_files('/media/user-data', prefix='user-data/')
