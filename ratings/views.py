from django.http import JsonResponse
import json
from django.shortcuts import render

def viewprofile(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Received data:", data)

            # Extracting data
            user_id = data.get('user_id')
            phone_number = data.get('phone')
            customer_id = data.get('customer_id')
            customer_name = data.get('customer_name')
            customer_phone = data.get('customer_phone')
            service_type = data.get('serviceType')

            print("User ID:", user_id)
            print("Phone Number:", phone_number)

            return JsonResponse({
                "success": True,
                "message": "Booking processed successfully!"
            })

        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=500)
    
    elif request.method == "GET":
        # Render the profile page on GET request
        return render(request, "ORDR.html")

    else:
        return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)