from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse('mysql://b23852204fe535:549d2848@eu-cdbr-west-01.cleardb.com/heroku_f520cf0b7d7fe79')

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_iNPNTHY1Zw5QiXrxNA37egOb')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_NehlxhN0uZdfo42GjhIhGI3C')

# Paypal environment variables
SITE_URL = 'https://nina-django-staging-1.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://nina-django-staging-1.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'mymerchant1@outlook.com'
