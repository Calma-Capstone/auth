import environ
import logging
env = environ.Env()

print("yoo")
print(env.db())
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}