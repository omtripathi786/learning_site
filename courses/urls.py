__author__ = 'om'

from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.course_list),
    url(r'(?P<pk>\d+)/$', views.course_detail),
]