from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from userauth.models import ServiceProvider, Customer
from SMS.utils import send_sms
import json

 # Temporary for debugging; ensure CSRF tokens are used in production
def book_service(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Received data:", data)

            user_id = data.get('user_id')
            phone_number = data.get('phone')
            print(f"User ID: {user_id}, Phone Number: {phone_number}")

            # Validate data
            if not user_id or not phone_number:
                return JsonResponse({"message": "Invalid data: user_id or phone is missing."}, status=400)

            # Get the service provider
            service_provider = get_object_or_404(ServiceProvider, user__id=user_id)
            print(f"Service Provider: {service_provider.user.kyc.name}")

            # Get the customer
            # customer = get_object_or_404(Customer, user=request.user)
            # customer_phone = customer.phone
            # print(f"Customer phone: {customer_phone}")

            # Create the SMS message
            message = f"Dear {service_provider.user.kyc.name}, you have a new service booking request from customer!"

            # Send SMS
            sms_response = send_sms(phone_number, message)
            print("SMS response:", sms_response)

            if sms_response.get("success"):
                return JsonResponse({"success": True, "message": "Booking successful. SMS sent!"})
            else:
                return JsonResponse({"success": False, "message": "Booking failed. Could not send SMS."}, status=400)
        except Exception as e:
            print("Error in book_service view:", str(e))
            return JsonResponse({"message": "An error occurred while processing your request."}, status=500)

    return JsonResponse({"message": "Invalid request method."}, status=400)