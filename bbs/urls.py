#https://noauto-nolife.com/post/startup-django/

from django.urls import path
from . import views

app_name = "bbs"
urlpatterns=[
    path('', views.index, name='index'),
    ]
