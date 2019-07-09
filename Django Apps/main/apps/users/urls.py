from django.conf.urls import url
from . import views 

from django.conf.urls import url
from . import views          

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.create_user),
    url(r'^create$', views.create),
    url(r'(?P<user_id>\d+)/$', views.show),
    url(r'(?P<user_id>\d+)/edit$', views.edit),
    url(r'(?P<user_id>\d+)/update$', views.update),
    url(r'(?P<user_id>\d+)/delete$', views.destroy)
]                            
