import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-b(1hjh-2(d*@g01au#jnz07l_9t%1s6s!jh)5rp-l@d-0(n@b&"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "polls.apps.PollsConfig",
    "mptt",
    "django_recaptcha",
    "debug_toolbar",
    "social_django",
    "django_extensions",
    "django.contrib.sitemaps",


]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "polls.middleware.RedirectAuthenticatedUserMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'freelibary',
        'USER': 'freelibary',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Irkutsk"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# email send
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_USE_SSL = True

EMAIL_HOST_USER = 'halitovmaxim@yandex.ru'
EMAIL_HOST_PASSWORD = 'bfelvvckaasesaec'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER
EMAIL_SERVER = 'masadropd1@gmail.com'

# end email send
SITE_ID = 1

INTERNAL_IPS = [
    '127.0.0.1',
]
CART_SESSION_ID = 'cart'

# social Django

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',  # бекенд авторизации через ВКонтакте
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_VK_OAUTH2_KEY = '51719070'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'RO1K1uNHbSGO9MWjRBhc'
LOGIN_REDIRECT_URL = '/'
# end social Django

# Расширенная модель User
AUTH_USER_MODEL = 'polls.User'
DEFAULT_USER_IMAGE = MEDIA_URL + 'users/default.jpg'
# Конец расширеной модели User

DOMAIN = '127.0.0.1:4000'

CACHES = {
    "default": {
        # "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, 'site_cache'),
    }
}

# GITHUB keys
SOCIAL_AUTH_GITHUB_KEY = '6fed2c99e288d6851633'
SOCIAL_AUTH_GITHUB_SECRET = '5e492a832518c16fdf897e796613284ffdba58a6'

# captcha keys
RECAPTCHA_PUBLIC_KEY = '6LcIR6EpAAAAACRFFYMbeR6xQQqclinJC8TxNx-R'
RECAPTCHA_PRIVATE_KEY = '6LcIR6EpAAAAAEnYEN1BZLJebmlApOnVXLGyS1_A'