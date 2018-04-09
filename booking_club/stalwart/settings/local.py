from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stalwart_accounts',
        'USER': 'accounts',
        'PASSWORD': 'accounts',
        'HOST': '127.0.0.1',
        'PORT': 3307
    }
}

REST_USE_JWT = True

JWT_ALLOW_REFRESH = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Booking Club'
EMAIL_HOST_PASSWORD = 'WenUW8n9NPxJ90P3wqEn5Q'
SERVER_EMAIL = 'debasishmath92@gmail.com'


DEBUG = True

