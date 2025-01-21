
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import KYC
from django.http import HttpResponseForbidden
@login_required
def kyc_form_view(request):
    if not request.user.is_ServiceProvider:
        return HttpResponseForbidden("You are not authorized to access this page.")
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        photo = request.FILES.get("photo")
        service_type = request.POST.get("service_type")
        
        citizenship_number = request.POST.get("citizenship_number")
        
        citizenship_photo = request.FILES.get("citizenship_photo")
        training_certificate = request.FILES.get("training_certificate")

        # Save KYC data
        kyc, created = KYC.objects.get_or_create(service_provider=request.user)
        kyc.name = name
        kyc.address = address
        kyc.service_type = service_type
        kyc.citizenship_number = citizenship_number
        kyc.photo = photo
        kyc.citizenship_photo = citizenship_photo
        kyc.training_certificate = training_certificate
        kyc.is_verified = False  # Ensure KYC starts as unverified
        kyc.save()

        return render(request, "kycverification.html", {"submitted": True})

    return render(request, "kycverification.html")