from django.shortcuts import render
from django.http import HttpResponse

def login (request):
    context = {}
    return render(request,'login/login.html',context)

def register (request):
    context = {}
    return render(request,'register/register.html',context)
