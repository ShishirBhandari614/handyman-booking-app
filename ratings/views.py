from django.shortcuts import render

# Create your views here.
def viewprofile(requests):
    return render(requests, "ORDR.html")