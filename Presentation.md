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

![alt text](https://github.com/marinar578/django/blob/ulyssesyang/django_vs_rails.png)

![alt text](https://github.com/marinar578/django/blob/ulyssesyang/django_mtv.png)

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

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

@python_2_unicode_compatible
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.answer_text

# views.py (the business logic) - MODEL

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import redirect

from .models import Answer, Question

class IndexView(generic.ListView):
    template_name = 'feedback/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'feedback/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'feedback/results.html'

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_answer = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'feedback/detail.html', {
            'question': question,
            'error_message': "You didn't select an answer.",
        })
    else:
        selected_answer.votes += 1
        selected_answer.save()
        return HttpResponseRedirect(reverse('feedback:results', args=(question.id,)))
        
# urls.py (the URL configuration) - CONTROLLER

from django.conf.urls import url

from . import views

app_name = 'feedback'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
]

# latest_books.html (the template) - VIEW

{% load staticfiles %}

<link rel="stylesheet" type="text/css" href="{% static 'feedback/style.css' %}" />

<div class="container">
    <h3>Django Feedback</h3>

    {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <div class="question">
            <li><a href="{% url 'feedback:detail' question.id %}">{{ question.question_text }}</a></li>
            <form action="{% url 'feedback:answer' question.id %}" method="post">
            {% csrf_token %}
            {% for answer in question.answer_set.all %}
                <input type="radio" name="answer" id="answer{{ forloop.counter }}" value="{{ answer.id }}" />
                <label for="answer{{ forloop.counter }}">{{ answer.answer_text }}</label><br />
            {% endfor %}
            <input type="submit" value="Answer" />
            </form>
            </div>
        {% endfor %}
        </ul>
    {% else %}
        <p>No feedback is available.</p>
    {% endif %}
</div>
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
### URL configuration

To bind a view function to a particular URL with Django, we use a URLconf in url.py files.

First we need to config the URL for the project: 

```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^feedback/', include('feedback.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('feedback.urls')),
]
```

For each specific app, we also need to config URL:

```
from django.conf.urls import url

from . import views

app_name = 'feedback'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
]
```
The variable urlpatterns, is a default variable that Django expects to find in a URLconf module. It calls the function patterns and saves the result into a variable that defines the mapping between URLs and the code that handles those URLs. 

The first argument passed into the patterns function is generally an empty string, but this string can be used to supply a common prefix for view functions.

The second argument line is referred to as a URLpattern. The url() function tells Django how to handle the url that you are configuring. The first argument is a pattern-matching string (a regular expression) and the second argument is the view function to use for that pattern. url() can take other optional arguments as well.

The 'r' character in front of the regular expression string tells Python that the string is a “raw string” – its contents should not interpret backslashes. In normal Python strings, backslashes are used for escaping special characters – such as in the string '\n', which is a one-character string containing a newline. When you add the r to make it a raw string, Python does not apply its backslash escaping – so, r'\n' is a two-character string containing a literal backslash and a lowercase “n”. There’s a natural collision between Python’s usage of backslashes and the backslashes that are found in regular expressions, so it’s strongly suggested that raw strings are used any time one is defining a regular expression in Python.

Finally, the pattern includes a caret (^) and a dollar sign ($). These are regular expression characters that have a special meaning: the caret means “require that the pattern matches the start of the string,” and the dollar sign means “require that the pattern matches the end of the string.” Had this not been included Django would match ANY URL that starts or ends with hello, such as `/hello/foo` or '/foo/bar/hello'. Thus, we use both the caret and dollar sign to ensure that only the URL /hello/ matches – nothing more, nothing less.

### Django URLconf vs Rails URLconf
In Rails, URLconf is in the routes.rb file under config folder. Rails makes building REST web services a breeze and routes are expressed in terms of HTTP verbs.
Django does not use the HTTP verb to route. Instead it is more verbose and uses regular expressions to match URLs to controllers. Django doesn’t have any convention when naming controller actions, so Django does not have any cool helpers like Rails’ resource and every route has to be explicitly defined. This results in each controller requiring several routing rules.


## Models && The Database
### settings.py
This is a normal Python module with module-level variables representing Django settings. By default, the configuration uses SQLite.

##### ENGINE
```
DATABASE = {
    'default': {
        # For sqLite
        'ENGINE': 'django.db.backends.sqlite3'
        
        # For PostgreSQL
        'ENGINE': 'django.db.backends.postgresql'
        
        # For MySQL
        'ENGINE': 'django.db.backends.mysql'
        
        # For Oracle
        'ENGINE': 'django.db.backends.oracle'
```
If you wish to use another database, install the appropriate database bindings and change the following keys in the DATABASES 'default' item to match your database connection settings. If you are not using SQLite as your database, additional settings such as USER, PASSWORD, and HOST must be added. For more details, see the reference documentation for DATABASES.

##### NAME
The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, os.path.join(BASE_DIR, 'db.sqlite3'), will store the file in your project directory.

##### MIGRATIONS
The INSTALLED_APPS hold the names of all Django applications that are activated in this Django instance. Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects. Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

```
python manage.py migrate
```

### models.py
```
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

=======================================
Debugging The Web App
=======================================
```
# Include the pdb module within the file structure
import pdb

# Call the module and run the 'set_trace' function
pdb.set_trace()
```