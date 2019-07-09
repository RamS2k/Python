from django.conf.urls import url
from . import views          

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^new$', views.new),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<year>[0-9]{4})/(edit)$', views.edit),
    url(r'^(?P<number>[0-9]{4})/(delete)$', views.destroy)
]                            
