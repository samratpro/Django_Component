# Creating Invirment
python -m venv env

# Active envirment
Source scripts/env/activate


#Commands---------------------------------------
# Django install..
pip install django

# Django Project Create..
django-admin startproject "projectname"

# Django App Creating..
python manage.py startapp "appname"

# Server Running..
python manage.py runserver     # python manage.py runserver 0.0.0.0:8000 --noreload

# Server Stop
# Ctrl + C


## Commands
delete db migrations or db
delete db
then delete all files from the migration folder of the app folder without __init__.py

# For database update
python manage.py makemigrations
python manage.py migrate

# For Admin
python manage.py createsuperuser


# Important folders..
templates
static

# For static update
python manage.py collectstatic

404 Page
# >>> 404.html and Debug is false for 404 page

# CSS JS support
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">
<script src="{% static 'myfirst.js' %}"></script>
