import environ
import os
import io

from Calma.settings.production.base import env
env.read_env(io.StringIO(os.environ.get("AUTH_SECRET", None)))

DATABASES = {
  'default': env.db()
}

# Change database settings if using the Cloud SQL Auth Proxy
if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
    DATABASES["default"]["HOST"] = "127.0.0.1"
    DATABASES["default"]["PORT"] = 5432
