from django.conf.urls import url
from . import views

app_name = 'polls'

# deal with the relative url within this app
urlpatterns = [

    # regex does no search domain name or the GET/POST parameters.
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]