from django.conf.urls import url
from . import views          

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^attempt$', views.attempt),
    url(r'^reset$', views.reset)
]                            
