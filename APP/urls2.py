from django.urls import path
from .views import *

urlpatterns = [
    path("milk/",index1 ),
    path("bread/", index2)
]