from .common import *

# SECRET CONFIGURATION
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY CONFIGURATION
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    'DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    'DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# ALLOWED HOSTS
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

# APPS
INSTALLED_APPS += ("gunicorn", )

# DATABASE
DATABASES = {'default': env.db("DATABASE_URL")}

# ADMIN URL
ADMIN_URL = env('DJANGO_ADMIN_URL')
