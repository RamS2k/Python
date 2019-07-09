from django.conf.urls import url
from . import views          

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^add_word$', views.add_word),
    url(r'^clear$', views.clear),
]