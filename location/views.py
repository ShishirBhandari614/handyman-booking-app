from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from location.models import CustomerLocation, ServiceProviderLocation


@csrf_protect
@login_required
def save_location(request):
    if request.method == 'POST':
       
        data = json.loads(request.body)
        user_type = data.get('user_type')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

       
        # Check if the user is associated with a customer or service provider
        if user_type == 'customer':
           
            if hasattr(request.user, 'customer'):
                customer = request.user.customer
                
                CustomerLocation.objects.update_or_create(
                    customer=customer,
                    defaults={'latitude': latitude, 'longitude': longitude},
                )
                return JsonResponse({'message': 'Customer location updated.'}, status=200)
            else:
                print(f"User {request.user} is not associated with a customer.")
                return JsonResponse({'error': 'Unauthorized access. No customer found.'}, status=400)

        elif user_type == 'service_provider':
            if hasattr(request.user, 'serviceprovider'):
                service_provider = request.user.serviceprovider
                ServiceProviderLocation.objects.update_or_create(
                    service_provider=service_provider,
                    defaults={'latitude': latitude, 'longitude': longitude},
                )
                return JsonResponse({'message': 'Service provider location updated.'}, status=200)
            else:
                print(f"User {request.user} is not associated with a service provider.")
                return JsonResponse({'error': 'Unauthorized access. No service provider found.'}, status=400)

        return JsonResponse({'error': 'Invalid user type or unauthorized access.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)



@login_required
def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        is_online = data.get('is_online')

        # Ensure the user is a service provider
        if hasattr(request.user, 'serviceprovider'):
            service_provider = request.user.serviceprovider
            
            # Update the 'is_online' field
            service_provider_location, created = ServiceProviderLocation.objects.update_or_create(
                service_provider=service_provider,
                defaults={'is_online': is_online}
            )

            return JsonResponse({'message': 'Service provider status updated.'}, status=200)

        return JsonResponse({'error': 'User is not a service provider.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
