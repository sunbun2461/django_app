Django app for PJi practice
----------------------------
thomasario@Thomass-MBP django_app% python3 -m venv dango_app_env
thomasario@Thomass-MBP django_app% source django_app_venv #to enter the environment
(django_app_venv) thomasario@Thomass-MBP django_app % django-admin startproject pji_dev_shop .

# new app (named shop in this case)
(django_app_venv) thomasario@Thomass-MBP django_app % python manage.py startapp shop

# add app to settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
]

# define models in model.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

 # migrate models to update schema database
(django_app_venv) thomasario@Thomass-MBP django_app % python manage.py makemigrations
(django_app_venv) thomasario@Thomass-MBP django_app % python manage.py migrate

# super user creation
(django_app_venv) thomasario@Thomass-MBP django_app % python manage.py createsuperuser
user: thomasario
email: a.thomas.rio@gmail.com
pass: Seagull221@

#  register models with admin site with admin.py
from .models import Product

admin.site.register(Product)

# runserver
(django_app_venv) thomasario@Thomass-MBP django_app % python manage.py runserver
# Starting development server at http://127.0.0.1:8000/

# pji_dev_shop_db
mysql> CREATE DATABASE pji_dev_shop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# install mysql
pip install mysqlclient
