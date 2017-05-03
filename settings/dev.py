from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_iNPNTHY1Zw5QiXrxNA37egOb')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_NehlxhN0uZdfo42GjhIhGI3C')

# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://a1abb6b4.ngrok.io/a-very-hard-to-guess-url/'  # here again!
PAYPAL_RECEIVER_EMAIL = 'mymerchant1@outlook.com'
