from django.urls import path
from .views import noc_list

urlpatterns = [
    path('nocs/', noc_list, name='noc_list'),
]