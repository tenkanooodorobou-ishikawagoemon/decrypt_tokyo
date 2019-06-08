from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path("", top, name = "top"),

    path("all_idol/", all_idol, name = "all_idol"),
    # To show the "Idol" page
    path("<int:idol_id>/", idol, name = "idol"),
    path("idol_page/", idol_page, name = "idol_page"),
    #=========TEST=============
    path("test/", test, name = "test"),
    path('index/', get_index, name='index')
    path('index/', get_index, name='index'),
    path('idol/', get_idol, name='idol'),
]
