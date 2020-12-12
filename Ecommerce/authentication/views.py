from django.shortcuts import render
from django.http import HttpResponse
from authentication.models import user

def login (request):
    context = {
        'user_name' : user.user_name,

    }
    return render(request,'login/login.html',context)

def register (request):
    context = {}
    return render(request,'register/register.html',context)
