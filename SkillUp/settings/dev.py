from ._base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret("DATABASE_NAME"),
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST':'127.0.0.1',
        'PORT':'5432',
    }
}