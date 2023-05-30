import environ
import os

env = environ.Env()
env.read_env()
DATABASES = {
  'default': env.db('DATABASE_URL')
}