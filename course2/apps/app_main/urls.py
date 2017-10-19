from django.conf.urls import url
from . import views
from .models import Course

urlpatterns = [
    url(r'^$',views.index),
    url(r'^process$',views.process),
    url(r'^remove/(?P<id>\d+)$',views.remove)
]
