## super user creation
(django_app_venv) thomasario@Thomass-MBP django_app % python manage.py createsuperuser
user: thomasario
email: a.thomas.rio@gmail.com
pass: Seagull221@



## SQL
brew services start mysql
mysql_secure_installation
login
mysql -u root -p


# pji_dev_shop_db
mysql> CREATE DATABASE pji_dev_shop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;



password Seagull221@


## server 

# dev server
(django_app_venv) thomasario@Thomass-MBP django_app % python manage.py runserver 



## template 

# variables 
My first name is {{ first_name }}. My last name is {{ last_name }}

With a context of {'first_name': 'John', 'last_name': 'Doe'}, this template renders to:

My first name is John. My last name is Doe.


# tags
{% %} if statement and such 

This definition is deliberately vague. For example, a tag can output content, serve as a control structure e.g. an “if” statement or a “for” loop, grab content from a database, or even enable access to other template tags.

{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}

# filters
{{ django|title}}
Filters transform the values of variables and tag arguments.

# comments 
{# this won't be rendered #}
{% this is multi-line %}

# components

get_template(template_name, using=None)
select_template(template_name_list,using=None)
exception TemplateDoesNoteExits(msg,tried=None,backend=None,chain=None)