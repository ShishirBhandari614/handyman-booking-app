from django.urls import path
from ratings.views import *
app_name='ratings'

urlpatterns = [
    path('viewprofile/', viewprofile, name='viewprofile'),   
]