"""
Django settings for askdjango project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'stq_+q_)t2z7jb-5%@q-td5&)%d!0)pw&d*h-e%p)&!mlws@)^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

# Add to app
    'blog',
    'dojo',
    'accounts',
    'shop',


# pip install
    'django_extensions',
    'debug_toolbar',
    'imagekit',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

#최상위 URLCONF
ROOT_URLCONF = 'askdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #프로젝트 전반적으로 쓰일 템플릿 파일의 경로를 지정.
            os.path.join(BASE_DIR, 'askdjango', 'templates'),
        ],
        'APP_DIRS': True,
        #accounts/templates/accounts/post_list.html
        #blog/templates/blog/post_list.html
        #dojo/templates/dojo/post_list.html
        #shop/templates/shop/post_list.html

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

WSGI_APPLICATION = 'askdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'askdjango', 'static')
    # 최상위에 둘 때
    # os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'


#상위 디렉터리에 저장 할 때
# MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#파일은 settings.MEDIA_ROOT경로에 저장되며,
#DB필드에는 settings.MEDIA_ROOT내 저장된 문자열을 저장함.





INTERNAL_IPS = ['127.0.0.1',]

# message framework custom
from django.contrib.messages import constants
MESSAGE_LEVEL = constants.DEBUG # 지금부터 debug 레벨의 messages 를 남길 수 있음.
MESSAGE_TAGS = {constants.ERROR:'danger'}




NAVER_CLIENT_ID = '9aFTtzF4oHR9HuI6_Gje'
# 필히 개별 client id를 지정해주세요.









