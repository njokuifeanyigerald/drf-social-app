from pathlib import Path
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-74w+f)47csbz+1xew)^6t55540-7tzsd!424aw!kj7e0r*ah0+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['DRF-Social-network-dev.ap-south-1.elasticbeanstalk.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',
    'account',


    'rest_framework',
    #CORS
    "corsheaders",



    # SIMPLEJWT
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

    'djoser'
]

AUTH_USER_MODEL = 'account.User'

# MOSTLY USED FOR DRF AUTHENTICATION
DJOSER = {
    'LOGIN_FIELD': 'email' ,
    # so someone can retype their password
    'USER_CREATE_PASSWORD_RETYPE': True,
    # automatically it is True, so i set it to False
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        # from the authentication app
        'user_create':  'account.serializers.UserCreationSerializer',
        'user': 'account.serializers.UserCreationSerializer',

        'user_delete' : 'djoser.serializers.UserDeleteSerializer',

    }
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=100),
    'ROTATE_REFRESH_TOKENS': False,
}
# SIMPLE_JWT = {
#     'AUTH_HEADER_TYPES': ('JWT',),
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=100),
#     'AUTH_TOKEN_CLASSES': (
#         'rest_framework_simplejwt.tokens.AccessToken',
#     )
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

CORS_ALLOW_ALL_ORIGINS = True


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # CORS HEADERS
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = 'social_job.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'social_job.wsgi.application'

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'awseb-e-vdxp3vxbkp-stack-awsebrdsdatabase-pe1o9kfoyqym',
        'USER': 'gerald',
        'PASSWORD': 'gerald2023',
        'HOST': 'awseb-e-vdxp3vxbkp-stack-awsebrdsdatabase-pe1o9kfoyqym.ctdsidsevol6.ap-south-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}

# DATABASES = {
#     "default": {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'socialNetwork',
#         'USER': 'postgres',
#         'PASSWORD': '12345',
#         'HOST': 'localhost'
#     }
# }
 

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
