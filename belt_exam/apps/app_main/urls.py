from django.conf.urls import url
from django.contrib import admin
from .import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^destination/(?P<id>\d+)$', views.destination),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^logout$', views.logout),
]
