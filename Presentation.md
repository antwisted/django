=======================================
Commands
=======================================

Test Django installation: (from python shell)
```
>>> import django
>>> django.VERSION
```

New Django project:
```
django-admin startproject mysite
```

Launch Django server:
```
python manage.py runserver [port_number] / [0.0.0.0:port_number]
```

=======================================
History
=======================================

Django grew organically from real-world applications written by a Web development team in Lawrence, Kansas, USA. It was born in the fall of 2003, when the Web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications.

The World Online team, responsible for the production and maintenance of several local news sites, thrived in a development environment dictated by journalism deadlines. For the sites – including LJWorld.com, Lawrence.com and KUsports.com – journalists (and management) demanded that features be added and entire applications be built on an intensely fast schedule, often with only days’ or hours’ notice. Thus, Simon and Adrian developed a time-saving Web development framework out of necessity – it was the only way they could build maintainable applications under the extreme deadlines.

In summer 2005, after having developed this framework to a point where it was efficiently powering most of World Online’s sites, the team, which now included Jacob Kaplan-Moss, decided to release the framework as open source software. They released it in July 2005 and named it Django, after the jazz guitarist Django Reinhardt.

Now, several years later, Django is a well-established open source project with tens of thousands of users and contributors spread across the planet. Two of the original World Online developers (the “Benevolent Dictators for Life,” Adrian and Jacob) still provide central guidance for the framework’s growth, but it’s much more of a collaborative team effort.

This history is relevant because it helps explain two key things. The first is Django’s “sweet spot.” Because Django was born in a news environment, it offers several features that are particularly well suited for “content” sites like Amazon.com, craigslist.org, and washingtonpost.com that offer dynamic, database-driven information. However, though Django is particularly good for developing those sorts of sites, that doesn’t preclude it from being an effective tool for building any sort of dynamic Web site.

The second matter to note is how Django’s origins have shaped the culture of its open source community. Because Django was extracted from real-world code, rather than being an academic exercise or commercial product, it is acutely focused on solving Web development problems that Django’s developers themselves have faced – and continue to face. As a result, Django itself is actively improved on an almost daily basis. The framework’s maintainers have a vested interest in making sure Django saves developers time, produces applications that are easy to maintain and performs well under load. If nothing else, the developers are motivated by their own selfish desires to save themselves time and enjoy their jobs.

- Courtesy of [The Django Book](http://www.djangobook.com)

=======================================
MVC Pattern Overview
=======================================

Model-View-Template in Django is an alternative to Model-View-Controller in RoR. Django view performs a role of a MVC controller as well as template of a Django is a MVC view.

![alt text](https://github.com/marinar578/django/blob/mahrtian/django.gif)

![alt text](https://github.com/marinar578/django/blob/mahrtian/django.gif)

=======================================
Intial Directory Structure
=======================================
```
File directory:
django/
    manage.py
    test_app/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

##### django/:
The outer mysite/ directory is just a container for this project. Its name doesn’t matter to Django; you can rename it to anything you like.

##### manage.py:
A command-line utility that lets you interact with this Django project in various ways. You should never have to edit this file; it’s created in this directory purely for convenience.

This file also manages your Python path; the list of directories on your system where Python looks when you use the Python import statement.

For example, let’s say your Python path is set to ['', '/usr/lib/python2.7/site-packages', '/home/username/zoolander'].
If you execute the Python statement:
```
from hello import world
```
Python will look for a module called hello.py in the current directory. If that file doesn’t exist, Python will look for the file /usr/lib/python2.7/site-packages/hello.py. If that file doesn’t exist, it will try /home/username/zoolander/hello.py. Finally, if that file doesn’t exist, it will raise ImportError.

To see your current path, type the following into your Python shell:
```
>>> import sys
>>> print sys.path
```

##### django/test_app/:
The inner directory test_app/ is the actual Python package for this project. Its name is the Python package name we'll need to use to import anything inside it (e.g. import test_app.settings).

##### __init__.py:
A file required for Python to treat the test_app directory as a package (i.e., a group of Python modules). It’s an empty file, and generally you won’t add anything to it.

##### settings.py:
Settings/configuration for this Django project. Like an extended Gemfile or Gemfile.lock, it contains types of settings available, along with their default values.

##### urls.py:
The URLs for this Django project. Think of this as the “table of contents”.

##### wsgi.py:
An entry-point for WSGI-compatible webservers to serve this project.

## Typical Division of Django MVC
```python
# models.py (the database tables)

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()


# views.py (the business logic) - MODEL

from django.shortcuts import render
from models import Book

def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render(request, 'latest_books.html', {'book_list': book_list})


# urls.py (the URL configuration) - CONTROLLER

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^latest/$', views.latest_books),
)


# latest_books.html (the template) - VIEW

<html><head><title>Books</title></head>
<body>
<h1>Books</h1>
<ul>
{% for book in book_list %}
<li>{{ book.name }}</li>
{% endfor %}
</ul>
</body></html>
```


=======================================
How Django Generates A Web App
=======================================

## Calling The View
### views.py
Django doesn’t care what the file is called – but it’s a good idea to call it views.py as a convention.

```
from django.http import HttpResponse
```
First, we import the class HttpResponse, which lives in the django.http module. We need to import this class because it’s used later in our code. Most .py files follow this convention; calling the file/module and importing the class(es) that's needed for its specific role in the functioning body.

```
def hello(request):
    return HttpResponse("Hello world")
```

Each view function takes at least one parameter, called request by convention. This is an object that contains information about the current Web request that has triggered this view, and it’s an instance of the class django.http.HttpRequest.

## Defining The Routes
### urls.py
To bind a view function to a particular URL with Django, we use a URLconf.

```
from django.conf.urls.defaults import patterns, url
from test_app.views import hello

urlpatterns = patterns('',
    url(r'^hello/$', hello),
)
```
The variable urlpatterns, is a default variable that Django expects to find in a URLconf module. It calls the function patterns and saves the result into a variable that defines the mapping between URLs and the code that handles those URLs. 

The first argument passed into the patterns function is generally an empty string, but this string can be used to supply a common prefix for view functions.

The second argument line is referred to as a URLpattern. The url() function tells Django how to handle the url that you are configuring. The first argument is a pattern-matching string (a regular expression) and the second argument is the view function to use for that pattern. url() can take other optional arguments as well.

The 'r' character in front of the regular expression string tells Python that the string is a “raw string” – its contents should not interpret backslashes. In normal Python strings, backslashes are used for escaping special characters – such as in the string '\n', which is a one-character string containing a newline. When you add the r to make it a raw string, Python does not apply its backslash escaping – so, r'\n' is a two-character string containing a literal backslash and a lowercase “n”. There’s a natural collision between Python’s usage of backslashes and the backslashes that are found in regular expressions, so it’s strongly suggested that raw strings are used any time one is defining a regular expression in Python.

Finally, the pattern includes a caret (^) and a dollar sign ($). These are regular expression characters that have a special meaning: the caret means “require that the pattern matches the start of the string,” and the dollar sign means “require that the pattern matches the end of the string.” Had this not been included Django would match ANY URL that starts or ends with hello, such as `/hello/foo` or '/foo/bar/hello'. Thus, we use both the caret and dollar sign to ensure that only the URL /hello/ matches – nothing more, nothing less.


## Models && The Database


=======================================
Debugging The Web App
=======================================
```
# Include the pdb module within the file structure
import pdb

# Call the module and run the 'set_trace' function
pdb.set_trace()
```