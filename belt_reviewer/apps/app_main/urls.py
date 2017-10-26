from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.registerNewUser),
    url(r'^login$', views.login),
    url(r'^books/add$', views.add),
]
