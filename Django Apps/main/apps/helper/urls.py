from django.conf.urls import url
from . import views          

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^add$', views.add),
    url(r'^add_jobs_page$', views.add_jobs_page),
    url(r'^load_dash$', views.load_dash),
    url(r'^logout$', views.logout),
    url(r'^delete/(?P<job_id>\d+)$', views.delete),
    url(r'^view/(?P<job_id>\d+)$', views.view),
    url(r'^edit_jobs_page/(?P<job_id>\d+)$', views.edit_jobs_page),
    url(r'^edit/(?P<job_id>\d+)$', views.edit),
    url(r'^add_my_job/(?P<job_id>\d+)$', views.add_my_job)
]