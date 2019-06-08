from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path("", top, name = "top"),
    #=========TEST=============
    path("test/", test, name = "test"),
    path('index/', get_index, name='index')
]
