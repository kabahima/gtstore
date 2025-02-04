from pathlib import Path
from decouple import config
import os
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Default for local development

if os.getenv("VERCEL"):
    DEBUG = False  # Disable DEBUG in production

ALLOWED_HOSTS = [
    '.vercel.app',
    '127.0.0.1',    
]

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


# use DEV_DATABASE to differentiate between dev and prod
# if config('DEV_DATABASE', default='sqlite') == 'postgresql':
    # Production database settings (PostgreSQL)
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT', default=5432, cast=int),
        }
    }
# else:
    # Development database settings (SQLite)
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }


# =========================
# Cloudinary Configuration
# =========================
# Cloudinary settings

cloudinary.config( 

    cloud_name= "ddubcf1rj",
    api_key="491932619944567",
    api_secret = "40ggngUkbSw-T9-nkW_aDVNLi3E",
    secure=True
)
   


# Set Cloudinary to handle media file storage
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

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
