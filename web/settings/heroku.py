from web.settings.base import *

import django_on_heroku
import os
import psycopg2
import dj_database_url
<<<<<<< HEAD
=======

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

django_on_heroku.settings(locals())
>>>>>>> 0d84c8f3c4e5bfcdc54352de9a661f3bbbbf9489

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

django_on_heroku.settings(locals())
