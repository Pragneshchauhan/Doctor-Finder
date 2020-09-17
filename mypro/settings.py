

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'df777',
        'USER': 'root',
        'PASSWORD':'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
EMAIL_USE_TLS =True
EMAIL_HOST ='smtp.gmail.com'
EMAIL_HOST_USER = 'Your Email-Id'
EMAIL_HOST_PASSWORD ='Password'
EMAIL_PORT = "emailport"
