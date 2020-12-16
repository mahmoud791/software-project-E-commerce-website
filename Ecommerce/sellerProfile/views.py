from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sellerProfile (request):
    return render(request,"sellerprofile/sellerprofile.html")