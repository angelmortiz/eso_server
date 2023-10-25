from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-!li*x__-7a@tc!o8a)0y6x^acyw(6%s6+i10sh!y$s)oi3ej(3'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eso_db_dev',
        'USER': 'esodev',
        'PASSWORD': 'esodevpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}