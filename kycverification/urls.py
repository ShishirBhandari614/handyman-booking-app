from django.urls import path
from kycverification.views import *
app_name='kycverification'

urlpatterns = [
    path('kyc-verification/', kyc_form_view, name='kyc_form_view'),
]