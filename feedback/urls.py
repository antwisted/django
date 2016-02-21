from django.conf.urls import url

from . import views

app_name = 'feedback'
urlpatterns = [
    # ex: /feedback/
    url(r'^$', views.index, name='index'),
    # ex: /feedback/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /feedback/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /feedback/5/answer/
    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
]