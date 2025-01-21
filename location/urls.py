from django.urls import path
from location.views import *
app_name='location'

urlpatterns = [
    path('savelocation/', save_location, name='save-location'),
    path('update-status/', update_status, name='update_status'),
]