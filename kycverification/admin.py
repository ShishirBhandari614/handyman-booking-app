from django.contrib import admin
from kycverification.models import KYC
@admin.register(KYC)
class KYCAdmin(admin.ModelAdmin):
    list_display = ('service_provider', 'is_verified', 'citizenship_number')
    list_filter = ('is_verified',)

# Register your models here.
