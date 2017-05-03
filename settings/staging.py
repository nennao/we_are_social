from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config("mysql://bc37ac631a2608:8aacc5cf@eu-cdbr-west-01.cleardb.com/heroku_49f54279425ad48?")

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_iNPNTHY1Zw5QiXrxNA37egOb')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_NehlxhN0uZdfo42GjhIhGI3C')

# Paypal environment variables
SITE_URL = 'https://nina-django-staging-1.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://nina-django-staging-1.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'mymerchant1@outlook.com'
