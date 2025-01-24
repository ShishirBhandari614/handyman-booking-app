from django.contrib import admin
from .models import *
@admin.register(Booking)
class bookingAdmin(admin.ModelAdmin):
    list_display=('customer','service_provider','service_type','booking_date','status')
# Register your models here.
