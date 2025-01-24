from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from userauth.models import ServiceProvider, Customer
from ratings.models import Booking  # Import your Booking model
from SMS.utils import send_sms
from django.utils.timezone import now
import json

@csrf_exempt  # Remove this in production and ensure CSRF tokens are handled
def book_service(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Received data:", data)

            user_id = data.get('user_id')
            phone_number = data.get('phone')
            customer_id = data.get('customer_id')
            customer_name = data.get('customer_name')
            customer_phone = data.get('customer_phone')
            service_type = data.get('serviceType')

            # Validate required data
            if not user_id or not phone_number or not customer_id:
                return JsonResponse({"message": "Invalid data: Missing required fields."}, status=400)

            # Get the service provider and customer
            service_provider = get_object_or_404(ServiceProvider, user__id=user_id)
            customer = get_object_or_404(Customer, user__id=customer_id)

            # Create a new booking record
            booking = Booking.objects.create(
                customer=customer,
                service_provider=service_provider,
                service_type=service_type,  # Assuming service type is available in the model
                booking_date=now(),
                status='pending'
            )

            # Create the SMS message with customer details
            message = (f"Dear {service_provider.user.kyc.name}, "
                       f"You have a new service booking request from {customer_name} "
                       f"(Phone: {customer_phone}). Please respond soon.")

            # Send SMS notification
            sms_response = send_sms(phone_number, message)
            print("SMS response:", sms_response)

            if sms_response.get("success"):
                return JsonResponse({"success": True, "message": "Booking successful. SMS sent!"})
            else:
                return JsonResponse({"success": False, "message": "Booking failed. Could not send SMS."}, status=400)

        except Exception as e:
            print("Error in book_service view:", str(e))
            return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)

    return JsonResponse({"message": "Invalid request method."}, status=400)
