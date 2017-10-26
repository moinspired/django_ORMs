from django.conf.urls import url
from django.contrib import admin
from .import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/new$', views.new_user),
    url(r'^session/new$', views.new_session),
]
