from pathlib import Path
from decouple import config
import os
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-dev-key-change-me')

DEBUG = config('DEBUG', default=True, cast=bool)

if os.getenv("VERCEL"):
    DEBUG = False

default_hosts = ['127.0.0.1', 'localhost']
if os.getenv('VERCEL'):
    default_hosts.append('.vercel.app')
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default=','.join(default_hosts),
    cast=lambda value: [host.strip() for host in value.split(',') if host.strip()],
)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage', 
    'products', 
    'accounts',
    'cart',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = ['accounts.authentication.CustomAuthBackend']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.app'


USE_SQLITE = config('USE_SQLITE', default=True, cast=bool)

if USE_SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME', default='gtstore'),
            'USER': config('DB_USER', default='postgres'),
            'PASSWORD': config('DB_PASSWORD', default=''),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', default=5432, cast=int),
        }
    }


# =========================
# Cloudinary Configuration
# =========================
# Cloudinary settings

cloudinary.config(
    cloud_name=config('CLOUDINARY_CLOUD_NAME', default='demo'),
    api_key=config('CLOUDINARY_API_KEY', default='demo'),
    api_secret=config('CLOUDINARY_API_SECRET', default='demo'),
    secure=True,
)

# Set Cloudinary to handle media file storage when configured; fall back to local storage otherwise.
if config('USE_CLOUDINARY', default=False, cast=bool):
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Static files (CSS, JavaScript, Images)
# ===================================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ensure this is pointing to the correct static folder for development
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Only for use in production when running collectstatic


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# WhatsApp Configuration
WHATSAPP_ORDER_NUMBER = config('WHATSAPP_ORDER_NUMBER', default='')
