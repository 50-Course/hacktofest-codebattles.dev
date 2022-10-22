"""
This module contains the 'Development' configurations.

NOTE: Never run this on staging or production server.
"""

import os

from settings.base import *
from settings.base import BASE_DIR

# We are for now using SQLite as our dev database.
# @TODO: Migrate to remote postgres DB.
DATABASES = {"ENGINE": "django.db.backends.sqlite3"}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
#
# To be configured differently in production

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
