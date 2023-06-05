from Calma.settings.components.base import REST_FRAMEWORK,INSTALLED_APPS
import environ
import os
import io
from urllib.parse import urlparse

env = environ.Env()
env.read_env(io.StringIO(os.environ.get("AUTH_SECRET", None)))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG", default=False)

# If defined, add service URL to Django security settings
CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)
if CLOUDRUN_SERVICE_URL:
    ALLOWED_HOSTS = [urlparse(CLOUDRUN_SERVICE_URL).netloc]
    CSRF_TRUSTED_ORIGINS = [CLOUDRUN_SERVICE_URL]
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
else:
    ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)
