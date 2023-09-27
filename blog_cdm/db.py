import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

# psycopg2
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog_produccion',
        'USER': 'postgre',
        'PASSWORD': '4#2!pOiUvCxZ',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}