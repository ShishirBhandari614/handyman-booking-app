from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.db import transaction
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_ServiceProvider = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.username
    

class ServiceProvider(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, related_name="serviceprovider")
    phone = models.CharField(max_length=10, blank=True)
    # email = models.EmailField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username
    
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)   
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created and instance:
#         Token.objects.create(user=instance)
        
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    phone = phone = models.CharField(max_length=10, blank=True)
    # email = models.EmailField(max_length=254, blank=True)
    
    def  __str__(self):
        return self.user.username
    
