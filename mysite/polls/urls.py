from django.conf.urls import url
from . import views

# deal with the relative url within this app
urlpatterns = [

    # regex does no search domain name or the GET/POST parameters.
    url(r'^$', views.index, name='index'),
]