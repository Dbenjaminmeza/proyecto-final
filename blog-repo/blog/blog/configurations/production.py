from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: configurar mi dominio al hacer deploy a produccion
ALLOWED_HOSTS = ['midominio-production.com']

#TO
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        
        # en caso de usar una posgres
        # 'ENGINE': 'django.db.backends.postgresql',

        # en caso de usar una mysql
        # 'ENGINE': 'django.db.backends.mysql',

        # 'NAME': os.getenv('DB_NAME'),

        # 'USER': os.getenv('DB_USER'),

        # 'PASSWORD': os.getenv('SECRET_KEY'),

        # 'HOST': os.getenv('DB_HOST'),
        
        # 'PORT': os.getenv('DB_PORT'),
    }
}

os.environ['DJANGO_PORT'] = '8080'
