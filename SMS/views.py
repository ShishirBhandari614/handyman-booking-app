from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from userauth.models import ServiceProvider, Customer
from SMS.utils import send_sms  # Assuming SMS function is in utils.py
import json
  # Use CSRF token in AJAX instead of this in production
def book_service(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data.get('user_id')
        phone_number = data.get('phone')
        print(f"Received user_id: {user_id}, phone_number: {phone_number}")
        # Get the service provider
        service_provider = get_object_or_404(ServiceProvider, user__id=user_id)

        # Get the customer’s phone number (assuming the logged-in user is the customer)
        customer = get_object_or_404(Customer, user=request.user)  # Assuming the customer is the logged-in user
        customer_phone = customer.phone

        # Create the SMS message
        message = f"Dear {service_provider.user.kyc.name}, you have a new service booking request from customer {customer_phone}!"

        # Send SMS
        sms_response = send_sms(phone_number, message)

        if sms_response.get("success"):
            return JsonResponse({"message": "Booking successful. SMS sent!"})
        else:
            return JsonResponse({"message": "Booking failed. Could not send SMS."}, status=400)

    return JsonResponse({"message": "Invalid request"}, status=400)
