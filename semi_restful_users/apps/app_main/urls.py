from django.conf.urls import include, url
from . import views
from . models import User
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/new$', views.add),
    url(r'^user/(?P<id>\d+)$',views.displayUser),
    url(r'^user/(?P<id>\d+)/edit$',views.editUser),
    url(r'^user/(?P<id>\d+)/delete$',views.remove),
]
