# Django Unchained

![alt text](https://github.com/marinar578/django/blob/mahrtian/django.gif)

Welcome to Django, a Python Web framework originally designed so that web professionals - namely those working in e-newsrooms - could "take applications from concept to completion" in as little time as possible and focus more on creating great content.

### Installfest

Before getting started with Django, you'll probably need to do the following.

##### 1. brew install python (OR brew update python)

Ensures that you have the latest version of Python on your computer (because Django is a Python Web framework). Upon **install** or **update**, you should have version 2.7.11.

##### 2. sudo easy_install pip

**pip** is a package management system used to install and manage software packages written in Python, and it’s what we’ll use to download Django (among other things). You will be prompted to enter your computer password to complete the download.

##### 3. pip install virtualenv

Creates isolated Python environments that have their own installation directories and don’t share libraries with other virtualenv environments.

##### 4. pip install virtualenvwrapper

Includes wrappers for creating and deleting virtual environments as well as managing development workflow (i.e. you can work on multiple projects without worrying about introducing dependency conflicts).

##### 5. pip install Django

This will, as the name suggests, install Django (it should be version 1.9.2). To verify that Django can be seen by python, type **python** in your CLI, followed by **import django** and **print(django.get_version())**. That should give you the version of Django you’re working with (i.e. what you just installed) in Python.

##### Optional Things to Install

  * **pip install mod_wsgi:** For when you’re ready to deploy Django in production (what we’re doing with this project is all in development). **mod_wsgi** embeds Python within Apache and loads Python code into memory when the server starts.

  * **pip install psycopg2:** Django automatically comes with SQLite capabilities, but what it you want to use PostgreSQL for larger products that you’ll eventually deploy? Installing the psycopg2 package allows for just that.

### "manage.py" Commands

When a Django project is created, a **manage.py** command-line utility is automatically created inside the project's outer directory. It allows users to interact with the project in various ways. The following are some of the more common interactions.

##### python manage.py shell

Opens the Python console. This command only works if you're in the aforementioned outer project directory.

##### python manage.py runserver

Runs the server and allows the Django project to be viewed in the browser's localhost.

##### Migrations

Database migrations in Django are very similar in their setup and execution to database migrations in Ruby and Ruby on Rails, although there are some slight differences in terms of execution.

  * **python manage.py migrate:** Creates any necessary database tables according to the database settings in the project's **settings.py** file (which is automatically created when the Django project is). It also executes any changes made later on to that database. Changes that are implemented through...

  * **python manage.py makemigrations <name of app>:** This creates new migrations based on the changes detected to your **models.py** file.

  * **python manage.py sqlmigrate <name of app> <migration number>:** This allows the user to view the complete SQL commands created by the aforementioned migrations.