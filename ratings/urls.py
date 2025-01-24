from django.urls import path
from ratings.views import *
app_name='location'

urlpatterns = [
    path('viewprofile/', viewprofile, name='viewprofile'),   
]