"""
WSGI config for pypoll project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pypoll.settings')

application = get_wsgi_application()



#Add static serving using whitenoise
#from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

#application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
