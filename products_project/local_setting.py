# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$0h2l&brnij4#l^#q=wx^e!)%ggkr3^^grdjdlbbyhc$9o!zc%'




# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD':'Password'
    }
}

