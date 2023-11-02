# Setting ------------------------------------------

# App connection..     # Probbaly 33 line
INSTALLED_APPS = [
    'NewApp',
]



# Template Connection..
DIRS': [BASE_DIR / 'templates'], # Probbaly 59 line


# Static File Connection..   # Probbaly 123 line
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles" # for collect static

# This is for Hosted server and When Debug is False after Hosting Django App in Domain
# >>> python manage.py collectstatic
# >>> Now configure Project urls.py
# >>> Or collect CSS and from `staticfiles` folder and paste it in `static` folder
# >>> Turn off/on Debug True/False and Restart app It will fix
# >>> If Debug is True then admin CSS won't work in the local Server
# >>> 404.html and Debug is false for 404 page


# For media support, also need to create ` media  ` in media >>> ` images ` folder where have manage.py 
# Also, need to Configure urls.py file for ` media support ` 
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Postgresql database  # Probbaly 78 line
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'samrat',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
    }
}
